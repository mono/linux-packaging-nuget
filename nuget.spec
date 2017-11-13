#
# spec file for package nuget
#
# Copyright (c) 2014 Xamarin, Inc (http://www.xamarin.com)
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

Name:           nuget
Version:        2.12+mono
Release:	0.xamarin.3
Summary:        Package manager for NuGet repositories
License:        MIT
Group:          Development/Libraries/Other
Url:            http://nuget.org/
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Source0:        nuget-%{version}.tar.xz
Source1:	nuget.sh
BuildRequires:  mono-devel
BuildArch:      noarch

%description
NuGet is the package manager for the Microsoft
development platform including .NET. The NuGet client
tools provide the ability to produce and consume
packages. The NuGet Gallery is the central package
repository used by all package authors and consumers.

%prep
%setup -n nuget-%{version}

%build
%{?exp_env}
%{?env_options}

%install
%{?env_options}
%{__mkdir_p} %{buildroot}%{_prefix}/lib/nuget
%{__mkdir_p} %{buildroot}%{_bindir}
%{__install} -m0755 %{SOURCE1} %{buildroot}%{_bindir}/`basename -s .sh %{SOURCE2}`
sed -i -e 's/cli/mono/' %{buildroot}%{_bindir}/*
%{__install} -m0755 nuget.exe %{buildroot}%{_prefix}/lib/nuget/

%files
%defattr(-,root,root)
%_prefix/lib/nuget
%_bindir/*

Name: cthon04
Version: 1
Release: 1%{?dist}
Summary: Connectathon Test Suite
License: Oracle
Group: Applications/System

Url: https://fedorapeople.org/cgit/steved/public_git/cthon04.git/
Source0: cthon04.tar
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)
Prefix: /opt

%description
Connectathon Test Suite (from Steve Dickson git repository)

%prep
%setup -q -n %{name}-%{version}

%build
make

%install
mkdir -p %{buildroot}/opt/cthon04
make copy DESTDIR=%{buildroot}/opt/cthon04

%files 
%defattr(-,root,root)
/opt/cthon04/*

%post 

%clean
[ $RPM_BUILD_ROOT != "/" ] && rm -fr $RPM_BUILD_ROOT


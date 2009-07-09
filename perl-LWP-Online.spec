%define upstream_name    LWP-Online
%define upstream_version 1.07

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:    Does your process have access to the web
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/LWP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(ExtUtils::MakeMaker)
BuildRequires: perl(LWP::Simple)
BuildRequires: perl(Test::More)
BuildRequires: perl(URI)
BuildArch: noarch
BuildRoot: %{_tmppath}/%{name}-%{version}-%{release}

%description
This module attempts to answer, as accurately as it can, one of the
nastiest technical questions there is.

*Am I on the internet?*

The answer is useful in a wide range of decisions. For example...

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README LICENSE Changes
%{_mandir}/man3/*
%perl_vendorlib/*



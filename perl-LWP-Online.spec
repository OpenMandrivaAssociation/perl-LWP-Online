%define upstream_name    LWP-Online
%define upstream_version 1.08

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Does your process have access to the web
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/LWP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(LWP::Simple)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(URI)
BuildArch:	noarch

%description
This module attempts to answer, as accurately as it can, one of the
nastiest technical questions there is.

*Am I on the internet?*

The answer is useful in a wide range of decisions. For example...

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc README LICENSE Changes
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Mon Jul 18 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.80.0-1mdv2011
+ Revision: 690273
- update to new version 1.08

* Mon Apr 18 2011 Funda Wang <fwang@mandriva.org> 1.70.0-3
+ Revision: 655037
- rebuild for updated spec-helper

* Mon Sep 28 2009 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-2mdv2011.0
+ Revision: 450475
- rebuild

* Thu Jul 09 2009 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-1mdv2010.0
+ Revision: 393746
- import perl-LWP-Online


* Thu Jul 09 2009 cpan2dist 1.07-1mdv
- initial mdv release, generated with cpan2dist

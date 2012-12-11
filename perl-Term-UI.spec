%define	upstream_name	 Term-UI
%define upstream_version 0.26

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Term::ReadLine UI made easy
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Log::Message::Simple)
BuildArch:	noarch

%description
"Term::UI" is a transparent way of eliminating the overhead of having to format
a question and then validate the reply, informing the user if the answer was
not proper and re-issuing the question.

Simply give it the question you want to ask, optionally with choices the user
can pick from and a default and "Term::UI" will DWYM.

For asking a yes or no question, there's even a shortcut.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Term/*
%{_mandir}/*/*


%changelog
* Mon Feb 28 2011 Funda Wang <fwang@mandriva.org> 0.260.0-2mdv2011.0
+ Revision: 640782
- rebuild to obsolete old packages

* Sat Feb 12 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.260.0-1
+ Revision: 637379
- update to new version 0.26

* Thu Feb 03 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.240.0-1
+ Revision: 635553
- update to new version 0.24

* Sat Jan 08 2011 Guillaume Rousse <guillomovitch@mandriva.org> 0.220.0-1mdv2011.0
+ Revision: 630636
- update to new version 0.22

* Tue Aug 04 2009 Jérôme Quelin <jquelin@mandriva.org> 0.200.0-1mdv2010.0
+ Revision: 408971
- rebuild using %%perl_convert_version

* Fri May 01 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.20-1mdv2010.0
+ Revision: 370185
- update to new version 0.20

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.18-1mdv2009.0
+ Revision: 136360
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Wed Nov 07 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.18-1mdv2008.1
+ Revision: 106664
- update to new version 0.18
- update to new version 0.18

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 0.16-1mdv2008.1
+ Revision: 97566
- update to new version 0.16

* Fri Jun 22 2007 Buchan Milne <bgmilne@mandriva.org> 0.14-1mdv2008.0
+ Revision: 42867
- Import perl-Term-UI



* Thu Jun 21 2007 Buchan Milne <bgmilne@mandriva.org> 0.14-1mdv2007.1
- initial package

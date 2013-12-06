%define	modname	Term-UI
%define modver 0.38

Summary:	Term::ReadLine UI made easy
Name:		perl-%{modname}
Version:	%perl_convert_version %{modver}
Release:	5
License:	Artistic/GPLv2
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{modname}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Term/Term-UI-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	perl-devel
BuildRequires:	perl(Log::Message::Simple)

%description
"Term::UI" is a transparent way of eliminating the overhead of having to format
a question and then validate the reply, informing the user if the answer was
not proper and re-issuing the question.

Simply give it the question you want to ask, optionally with choices the user
can pick from and a default and "Term::UI" will DWYM.

For asking a yes or no question, there's even a shortcut.

%prep
%setup -qn %{modname}-%{modver}

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
%{_mandir}/man3/*



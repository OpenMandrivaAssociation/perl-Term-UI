%define	modname	Term-UI
%define modver 0.50

Summary:	Term::ReadLine UI made easy
Name:		perl-%{modname}
Version:	%{modver}
Release:	1
License:	Artistic/GPLv2
Group:		Development/Perl
Url:		https://github.com/jib/term-ui
Source0:	https://cpan.metacpan.org/authors/id/B/BI/BINGOS/Term-UI-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl-devel
BuildRequires:	perl(Log::Message::Simple)
BuildRequires:	perl(Test::More)

%description
"Term::UI" is a transparent way of eliminating the overhead of having to format
a question and then validate the reply, informing the user if the answer was
not proper and re-issuing the question.

Simply give it the question you want to ask, optionally with choices the user
can pick from and a default and "Term::UI" will DWYM.

For asking a yes or no question, there's even a shortcut.

%prep
%autosetup -p1 -n %{modname}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
make test

%install
%make_install

%files
%doc README
%{perl_vendorlib}/Term/*
%doc %{_mandir}/man3/*

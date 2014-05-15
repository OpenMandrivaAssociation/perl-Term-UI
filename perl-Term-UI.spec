%define	upstream_name	 Term-UI
%define upstream_version 0.42

Name:		perl-%{upstream_name}
Version:	%perl_convert_version 0.42
Release:	1

Summary:	Term::ReadLine UI made easy
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org:21/pub/CPAN/modules/by-module/Term/Term-UI-0.42.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Log::Message::Simple)
BuildRequires:	perl(JSON::PP)
BuildRequires:	perl
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
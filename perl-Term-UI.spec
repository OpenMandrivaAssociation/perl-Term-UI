%define	upstream_name	 Term-UI
%define upstream_version 0.24

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	Term::ReadLine UI made easy
License:	Artistic/GPL
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Term/%{upstream_name}-%{upstream_version}.tar.gz

%if %{mdkversion} < 1010
BuildRequires:	perl-devel >= 5.8.1
%endif
BuildRequires:	perl(Log::Message::Simple)
BuildArch:	noarch
Buildroot:	%{_tmppath}/%{name}-%{version}-%{release}

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
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%__make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Term/*
%{_mandir}/*/*

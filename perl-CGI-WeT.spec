%include	/usr/lib/rpm/macros.perl
Summary:	CGI-WeT perl module
Summary(pl):	Modu� perla CGI-WeT
Name:		perl-CGI-WeT
Version:	0.71
Release:	4
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI-WeT-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	mod_perl
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-WeT - Suite of modules to themeify a website.

%description -l pl
CGI-WeT - zestaw modu��w do budowania stron www z mo�liwo�ci� wyboru
ich wygl�du.

%prep
%setup -q -n CGI-WeT-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -a scripts themes $RPM_BUILD_ROOT%{_examplesdir}/%{name}

gzip -9nf Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/CGI/WeT.pm
%{perl_sitelib}/CGI/WeT
%{_mandir}/man3/*
%{_examplesdir}/%{name}

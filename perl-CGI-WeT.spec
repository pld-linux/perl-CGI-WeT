%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	WeT
Summary:	CGI-WeT perl module
Summary(pl):	Modu³ perla CGI-WeT
Name:		perl-CGI-WeT
Version:	0.71
Release:	7
License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.cpan.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildRequires:	apache-mod_perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-WeT - Suite of modules to themeify a website.

%description -l pl
CGI-WeT - zestaw modu³ów do budowania stron www z mo¿liwo¶ci± wyboru
ich wygl±du.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

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

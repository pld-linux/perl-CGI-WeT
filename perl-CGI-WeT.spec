%include	/usr/lib/rpm/macros.perl
Summary:	CGI-WeT perl module
Summary(pl):	Modu³ perla CGI-WeT
Name:		perl-CGI-WeT
Version:	0.71
Release:	2
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI-WeT-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
BuildRequires:	perl-ldap
BuildRequires:	mod_perl
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-WeT - Suite of modules to themeify a website.

%description -l pl
CGI-WeT - zestaw modu³ów do budowania stron www z mo¿liwo¶ci± wyboru
ich wygl±du.

%prep
%setup -q -n CGI-WeT-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -a {scripts,themes} $RPM_BUILD_ROOT%{_prefix}/src/examples/%{name}

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/CGI/WeT
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv -f .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        Changes README

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {Changes,README}.gz

%{perl_sitelib}/CGI/WeT.pm
%{perl_sitelib}/CGI/WeT
%{perl_sitearch}/auto/CGI/WeT

%{_mandir}/man3/*

%{_prefix}/src/examples/%{name}

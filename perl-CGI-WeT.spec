%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	WeT
Summary:	CGI::WeT Perl module
Summary(cs):	Modul CGI::WeT pro Perl
Summary(da):	Perlmodul CGI::WeT
Summary(de):	CGI::WeT Perl Modul
Summary(es):	Módulo de Perl CGI::WeT
Summary(fr):	Module Perl CGI::WeT
Summary(it):	Modulo di Perl CGI::WeT
Summary(ja):	CGI::WeT Perl ¥â¥¸¥å¡¼¥ë
Summary(ko):	CGI::WeT ÆÞ ¸ðÁÙ
Summary(no):	Perlmodul CGI::WeT
Summary(pl):	Modu³ Perla CGI::WeT
Summary(pt):	Módulo de Perl CGI::WeT
Summary(pt_BR):	Módulo Perl CGI::WeT
Summary(ru):	íÏÄÕÌØ ÄÌÑ Perl CGI::WeT
Summary(sv):	CGI::WeT Perlmodul
Summary(uk):	íÏÄÕÌØ ÄÌÑ Perl CGI::WeT
Summary(zh_CN):	CGI::WeT Perl Ä£¿é
Name:		perl-CGI-WeT
Version:	0.71
Release:	10
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	78528519a7a96511b96064d9a4d750ce
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-devel >= 5.6
BuildRequires:	apache-mod_perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::WeT - Suite of modules to themeify a website.

%description -l pl
CGI::WeT - zestaw modu³ów do budowania stron www z mo¿liwo¶ci± wyboru
ich wygl±du.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

cp -a scripts themes $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_sitelib}/CGI/WeT.pm
%{perl_sitelib}/CGI/WeT
%{_mandir}/man3/*
%{_examplesdir}/%{name}

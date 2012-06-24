#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	WeT
Summary:	CGI::WeT Perl module - suite of modules to themeify a website
Summary(pl):	Modu� Perla CGI::WeT - pakiet modu��w do nadania motyw�w stronom WWW
Name:		perl-CGI-WeT
Version:	0.71
Release:	10
License:	Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	78528519a7a96511b96064d9a4d750ce
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	apache-mod_perl
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
The collection of CGI::WeT::* modules allows a site to be built from
three major components:
(1) static themed HTML files,
(2) theme definitions,
(3) CGI scripts.

%description -l pl
Zestaw modu��w CGI::WeT umo�liwia zbudowanie stron www z trzech
podstawiowych sk�adnik�w:
(1) statycznych plik�w HTML z motywami,
(2) definicji motyw�w,
(3) skrypt�w CGI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT
cp -a scripts themes $RPM_BUILD_ROOT%{_examplesdir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/CGI/WeT.pm
%{perl_vendorlib}/CGI/WeT
%{_mandir}/man3/*
%{_examplesdir}/%{name}

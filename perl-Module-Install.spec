#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Module
%define	pnam	Install
Summary:	Module::Install - Standalone, extensible Perl module installer
Summary(pl.UTF-8):	Module::Install - samodzielny, rozszerzalny instalator modułów Perla
Name:		perl-Module-Install
Version:	1.12
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Module/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	bc1d30e2f5d4a77c3645243d1849c074
URL:		http://search.cpan.org/dist/Module-Install/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Archive-Tar >= 1.44
BuildRequires:	perl-Devel-PPPort >= 3.16
BuildRequires:	perl-ExtUtils-Install >= 1.52
BuildRequires:	perl-ExtUtils-MakeMaker >= 6.59
BuildRequires:	perl-ExtUtils-ParseXS >= 2.19
BuildRequires:	perl-File-Remove >= 1.42
BuildRequires:	perl-JSON >= 2.14
BuildRequires:	perl-Module-Build >= 0.29
BuildRequires:	perl-Module-CoreList >= 2.17
BuildRequires:	perl-Module-ScanDeps >= 0.89
BuildRequires:	perl-PAR-Dist >= 0.29
BuildRequires:	perl-Parse-CPAN-Meta >= 1.39
BuildRequires:	perl-PathTools >= 3.28
BuildRequires:	perl-Test-Harness >= 3.13
BuildRequires:	perl-Test-Simple >= 0.86
BuildRequires:	perl-YAML-Tiny >= 1.38
BuildRequires:	perl-libwww >= 5.812
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Module::Install is a package for writing installers for CPAN (or
CPAN-like) distributions that are clean, simple, minimalist, act in a
strictly correct manner with both the ExtUtils::MakeMaker and
Module::Build build systems, and will run on any Perl installation
version 5.004 or newer.

The intent is to make it as easy as possible for CPAN authors (and
especially for first-time CPAN authors) to have installers that follow
all the best practices for distribution installation, but involve as
much DWIM (Do What I Mean) as possible when writing them.

%description -l pl.UTF-8
Module::Install to pakiet do pisania dla dystrybucji CPAN (lub
podobnych) instalatorów, które będą przejrzyste, minimalistyczne i
działały całkowicie poprawnie z systemami budowania
ExtUtils::MakeMaker i Module::Build, a także będą działać na każdej
instalacji Perla od wersji 5.004.

Celem jest jak największe ułatwienie autorom CPAN (a szczególnie
początkującym autorom CPAN) posiadania instalatorów zachowujących się
jak najlepiej.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	--skipdeps \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Module/Install.pod

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Module/AutoInstall.pm
%{perl_vendorlib}/Module/Install.pm
%{perl_vendorlib}/Module/Install
%dir %{perl_vendorlib}/inc
%dir %{perl_vendorlib}/inc/Module
%{perl_vendorlib}/inc/Module/Install.pm
%{perl_vendorlib}/inc/Module/Install
%{_mandir}/man3/Module::AutoInstall.3pm*
%{_mandir}/man3/Module::Install*.3pm*
%{_mandir}/man3/inc::Module::Install*.3pm*

#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Module
%define	pnam	Install
Summary:	Module::Install - Standalone, extensible Perl module installer
#Summary(pl):	
Name:		perl-Module-Install
Version:	0.63
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/A/AD/ADAMK/Module-Install-0.63.tar.gz
# Source0-md5:	d2404a019eaf149eaa34db65ab8fb72d
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-YAML >= 0.35
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

#%define         _noautoreq      'perl(inc::Module::Install)'

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

# %description -l pl
# TODO

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

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Module/*.pm
%{perl_vendorlib}/Module/Install
%{perl_vendorlib}/inc
%{_mandir}/man3/*

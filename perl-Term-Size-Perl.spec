#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	Term
%define	pnam	Size-Perl
Summary:	Term::Size::Perl - Perl extension for retrieving terminal size (Perl version)
#Summary(pl.UTF-8):
Name:		perl-Term-Size-Perl
Version:	0.029
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Term/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	e647aed35b0c4973e949c311a8222dbf
URL:		http://search.cpan.org/dist/Term-Size-Perl/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Yet another implementation of Term::Size. Now in pure Perl, with the
exception of a C probe run on build time.

# %description -l pl.UTF-8

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Term/Size/*.pm
%{perl_vendorlib}/Term/Size/Perl
%{_mandir}/man3/*

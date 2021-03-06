#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-App-perlbrew
Version  : 0.92
Release  : 17
URL      : https://cpan.metacpan.org/authors/id/G/GU/GUGOD/App-perlbrew-0.92.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/G/GU/GUGOD/App-perlbrew-0.92.tar.gz
Summary  : 'Manage perl installations in your C<$HOME>'
Group    : Development/Tools
License  : MIT
Requires: perl-App-perlbrew-bin = %{version}-%{release}
Requires: perl-App-perlbrew-license = %{version}-%{release}
Requires: perl-App-perlbrew-man = %{version}-%{release}
Requires: perl-App-perlbrew-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(ExtUtils::Config)
BuildRequires : perl(ExtUtils::Helpers)
BuildRequires : perl(ExtUtils::InstallPaths)
BuildRequires : perl(Module::Build::Tiny)

%description
NAME
App::perlbrew - Manage perl installations in your $HOME
SYNOPSIS
# Installation
curl -L https://install.perlbrew.pl | bash

# Initialize
perlbrew init

# See what is available
perlbrew available

# Install some Perls
perlbrew install 5.32.1
perlbrew install perl-5.28.3
perlbrew install perl-5.33.6

# See what were installed
perlbrew list

# Swith to an installation and set it as default
perlbrew switch perl-5.32.1

# Temporarily use another version only in current shell.
perlbrew use perl-5.28.3
perl -v

# Turn it off and go back to the system perl.
perlbrew off

# Turn it back on with 'switch', or 'use'
perlbrew switch perl-5.32.1
perlbrew use perl-5.32.1

# Exec something with all perlbrew-ed perls
perlbrew exec -- perl -E 'say $]'

%package bin
Summary: bin components for the perl-App-perlbrew package.
Group: Binaries
Requires: perl-App-perlbrew-license = %{version}-%{release}

%description bin
bin components for the perl-App-perlbrew package.


%package dev
Summary: dev components for the perl-App-perlbrew package.
Group: Development
Requires: perl-App-perlbrew-bin = %{version}-%{release}
Provides: perl-App-perlbrew-devel = %{version}-%{release}
Requires: perl-App-perlbrew = %{version}-%{release}

%description dev
dev components for the perl-App-perlbrew package.


%package license
Summary: license components for the perl-App-perlbrew package.
Group: Default

%description license
license components for the perl-App-perlbrew package.


%package man
Summary: man components for the perl-App-perlbrew package.
Group: Default

%description man
man components for the perl-App-perlbrew package.


%package perl
Summary: perl components for the perl-App-perlbrew package.
Group: Default
Requires: perl-App-perlbrew = %{version}-%{release}

%description perl
perl components for the perl-App-perlbrew package.


%prep
%setup -q -n App-perlbrew-0.92
cd %{_builddir}/App-perlbrew-0.92

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-App-perlbrew
cp %{_builddir}/App-perlbrew-0.92/LICENSE %{buildroot}/usr/share/package-licenses/perl-App-perlbrew/3f12f928da67f22daa38e4df02a3c1640d1fbcd1
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/perlbrew

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/App::Perlbrew::Path.3
/usr/share/man/man3/App::Perlbrew::Path::Installation.3
/usr/share/man/man3/App::Perlbrew::Path::Installations.3
/usr/share/man/man3/App::Perlbrew::Path::Root.3
/usr/share/man/man3/App::Perlbrew::Util.3
/usr/share/man/man3/App::perlbrew.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-App-perlbrew/3f12f928da67f22daa38e4df02a3c1640d1fbcd1

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/perlbrew.1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.34.0/App/Perlbrew/Path.pm
/usr/lib/perl5/vendor_perl/5.34.0/App/Perlbrew/Path/Installation.pm
/usr/lib/perl5/vendor_perl/5.34.0/App/Perlbrew/Path/Installations.pm
/usr/lib/perl5/vendor_perl/5.34.0/App/Perlbrew/Path/Root.pm
/usr/lib/perl5/vendor_perl/5.34.0/App/Perlbrew/Util.pm
/usr/lib/perl5/vendor_perl/5.34.0/App/perlbrew.pm

%define upstream_name	 Module-Reload
%define upstream_version 1.07

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2

Summary:	Reload %%INC files when updated on disk
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Module/%{upstream_name}-%{upstream_version}.tar.bz2

BuildRequires:	perl-devel
BuildArch:	noarch

%description
When Perl pulls a file via C<require>, it stores the filename in the
global hash C<%%INC>.  The next time Perl tries to C<require> the same
file, it sees the file in C<%%INC> and does not reload from disk.  This
module's handler iterates over C<%%INC> and reloads the file if it has
changed on disk. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc README
%{perl_vendorlib}/Module
%{_mandir}/man3/*

%changelog
* Wed Aug 05 2009 Jérôme Quelin <jquelin@mandriva.org> 1.70.0-1mdv2010.0
+ Revision: 410093
- rebuild using %%perl_convert_version

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 1.07-2mdv2009.0
+ Revision: 136290
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Jun 03 2007 Anssi Hannula <anssi@mandriva.org> 1.07-2mdv2008.0
+ Revision: 34870
- annual rebuild


* Sun May 28 2006 Anssi Hannula <anssi@mandriva.org> 1.07-1mdv2007.0
- initial Mandriva package


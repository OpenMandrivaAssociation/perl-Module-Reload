
%define module	Module-Reload
%define name	perl-%{module}
%define version	1.07
%define rel	2

Summary:	Reload %%INC files when updated on disk
Name:		%{name}
Version:	%{version}
Release:	%mkrel %{rel}
License:	GPL or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Module/%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel
BuildRoot:	%{_tmppath}/%{name}-%{version}
BuildArch:	noarch

%description
When Perl pulls a file via C<require>, it stores the filename in the
global hash C<%%INC>.  The next time Perl tries to C<require> the same
file, it sees the file in C<%%INC> and does not reload from disk.  This
module's handler iterates over C<%%INC> and reloads the file if it has
changed on disk. 

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc README
%{perl_vendorlib}/Module
%{_mandir}/man3/*


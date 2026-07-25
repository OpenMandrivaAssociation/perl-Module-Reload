%define upstream_name	 Module-Reload
%define upstream_version 1.12

Name:		perl-%{upstream_name}
Version:	%{upstream_version}
Release:	1

Summary:	Reload %%INC files when updated on disk
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://github.com/neilb/Module-Reload
Source0:	https://cpan.metacpan.org/authors/id/N/NE/NEILB/Module-Reload-%{upstream_version}.tar.gz
Source1:        %{name}.rpmlintrc

BuildRequires:	make
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

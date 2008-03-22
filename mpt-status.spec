Summary:	Program to print the status of an LSI 1030 RAID controller
Summary(pl.UTF-8):	Program podający stan kontrolera LSI 1030 RAID
Name:		mpt-status
Version:	1.2.0
Release:	2
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.drugphish.ch/~ratz/mpt-status/%{name}-%{version}.tar.bz2
# Source0-md5:	fae044db1340fd37aa81b4ecef7bbd46
# needed headers taken from kernel 2.6.16.29 source
Patch0:		%{name}-headers.patch
Patch1:		%{name}-no_compiler.h.patch
Patch2:		%{name}-sync_info.patch
URL:		http://www.red-bean.com/~mab/mpt-status.html
BuildRequires:	pciutils-devel
Requires:	dev >= 2.9.0-20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Program to print the status of an LSI 1030 RAID controller.

%description -l pl.UTF-8
Program podający stan kontrolera LSI 1030 RAID.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
%patch2 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -W -Iincl -Iinclude" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_mandir}/man8}

install mpt-status $RPM_BUILD_ROOT%{_bindir}
install man/mpt-status.8 $RPM_BUILD_ROOT%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{AUTHORS,Changelog,README,THANKS,ReleaseNotes}
%attr(755,root,root) %{_bindir}/mpt-status
%{_mandir}/man8/mpt-status.8*

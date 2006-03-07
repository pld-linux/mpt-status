Summary:	Program to print the status of an LSI 1030 RAID controller
Summary(pl):	Program podaj±cy stan kontrolera LSI 1030 RAID
Name:		mpt-status
Version:	1.1.6
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.drugphish.ch/~ratz/mpt-status/%{name}-%{version}.tar.bz2
# Source0-md5:	0758574317e9a32e9622c36820f6796f
# needed headers taken from kernel 2.4.31 source
Patch0:		%{name}-headers.patch
URL:		http://www.red-bean.com/~mab/mpt-status.html
BuildRequires:	pciutils-devel
Requires:	dev >= 2.9.0-20
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Program to print the status of an LSI 1030 RAID controller.

%description -l pl
Program podaj±cy stan kontrolera LSI 1030 RAID.

%prep
%setup -q
%patch0 -p1

%build
%{__make} \
	CC="%{__cc}" \
	CFLAGS="%{rpmcflags} -Wall -W -Iincl -Iinclude" \
	LDFLAGS="%{rpmldflags}"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install mpt-status $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc doc/{AUTHORS,Changelog,README,THANKS,ReleaseNotes}
%attr(755,root,root) %{_bindir}/*

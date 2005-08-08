Summary:	Program to print the status of an LSI 1030 RAID controller
Summary(pl):	Program podaj±cy stan kontrolera LSI 1030 RAID
Name:		mpt-status
Version:	1.0
Release:	1
License:	GPL v2+
Group:		Applications/System
Source0:	http://www.red-bean.com/~mab/%{name}-%{version}.tar.gz
# Source0-md5:	ab4d6ee64fe15ad34aa7a4aca22e5420
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
	CFLAGS="%{rpmcflags} -Wall -Iinclude"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_bindir}

install mpt-status $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*

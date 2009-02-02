Summary:	Program to print the status of an LSI RAID controllers
Summary(pl.UTF-8):	Program podający stan kontrolerów LSI RAID
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
The mpt-status software is a query tool to access the running
configuration and status of LSI SCSI HBAs. This is a completely
rewritten version of the original mpt-status-1.0 tool written by Matt
Braithwaite. mpt-status allows you to monitor the health and status of
your RAID setup. 

Currently supported and tested HBAs are:
- LSI 1030 SCSI RAID storage controller
- LSI SAS1064 SCSI RAID storage controller
- LSI SAS1068 SCSI RAID storage controller
- LSI SAS 3442-R SCSI RAID storage controller

Since the tool is using the MPI (message passing interface) chances
are high that the basic information regarding RAID status will be
available for all LSI based controllers. Just give it a try and report
back.

%description -l pl.UTF-8
Program mpt-status to narzędzie pozwalające na dostęp do konfiguracji
i stanu działających kontrolerów (HBA) SCSI firmy LSI. Jest to
napisana całkowicie od nowa wersja oryginalnego narzędzia
mpt-status-1.0 autorstwa Matta Braithwaite. mpt-status pozwala
monitorować stan macierzy RAID.

Aktualnie obsługiwane i przetestowane kontrolery to:
- LSI 1030 SCSI RAID storage controller
- LSI SAS1064 SCSI RAID storage controller
- LSI SAS1068 SCSI RAID storage controller
- LSI SAS 3442-R SCSI RAID storage controller

Ponieważ narzędzie używa interfejsu MPI (Message Passing Interface),
są duże szanse, że podstawowe informacje o stanie macierzy będą
dostępne dla wszystkich kontrolerów opartych na LSI. Zalecane jest
sprawdzenie i zgłoszenie informacji do autorów.

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

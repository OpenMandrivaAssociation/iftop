%define name iftop 
%define version 0.17
%define release 9

Name: %name
Summary: Command line tool that displays bandwidth usage on an interface
Version: %version
Release: %release
Source0: http://www.ex-parrot.com/~pdw/iftop/download/%{name}-%{version}.tar.bz2
Patch0: iftop-0.17-format_not_a_string_literal_and_no_format_arguments.diff
URL: http://www.ex-parrot.com/~pdw/iftop/ 
Group: Monitoring 
License: GPLv2
BuildRequires: libpcap-devel pkgconfig(ncurses) texinfo

%description
iftop does for network usage what top(1) does for CPU usage. It listens to
network traffic on a named interface and displays a table of current bandwidth
usage by pairs of hosts. Handy for answering the question "why is our ADSL link
so slow?".

%prep
%setup -q
%patch0 -p0

%build
%configure
%make

%install
mkdir -p %{buildroot}%{_sbindir} ${RPM_BUILD_ROOT}%{_mandir}/man8
install -m755 iftop %{buildroot}%{_sbindir}
install -m 644 iftop.8 ${RPM_BUILD_ROOT}%{_mandir}/man8

%files
%defattr(-,root,root,0755)
%{_sbindir}/iftop
%doc README COPYING TODO INSTALL
%{_mandir}/man8/*

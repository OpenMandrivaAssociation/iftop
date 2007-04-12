%define name iftop 
%define version 0.17
%define release %mkrel 2

Name: %name
Summary: Command line tool that displays bandwidth usage on an interface
Version: %version
Release: %release
Source: http://www.ex-parrot.com/~pdw/iftop/download/%{name}-%{version}.tar.bz2
URL: http://www.ex-parrot.com/~pdw/iftop/ 
Group: Monitoring 
BuildRoot: %{_tmppath}/%{name}-buildroot
License: GPL
BuildRequires: libpcap-devel libncurses-devel texinfo

%description
iftop does for network usage what top(1) does for CPU usage. It listens to
network traffic on a named interface and displays a table of current bandwidth
usage by pairs of hosts. Handy for answering the question "why is our ADSL link
so slow?".

%prep
rm -rf $RPM_BUILD_ROOT
%setup -q

%build
%configure
%make

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT%{_sbindir} ${RPM_BUILD_ROOT}%{_mandir}/man8
install -m755 iftop $RPM_BUILD_ROOT%{_sbindir}
install -m 644 iftop.8 ${RPM_BUILD_ROOT}%{_mandir}/man8

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,0755)
%{_sbindir}/iftop
%doc README COPYING TODO INSTALL
%{_mandir}/man8/*



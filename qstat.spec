#
# TODO:
# - pl desc
#
Summary:	Game server browsing utility (mostly FPP/FPS)
summary(pl):	Przeglądarka serwerów gier (głównie FPP/FPS)
Name:		qstat
Version:	2.5c
Release:	1
License:	Artistic
Group:		Applications/Games
Source0:	http://www.qstat.org/%{name}25c.tar.gz
# Source0-md5:	a936dc3e15ece567378a026737fe45e2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
qstat is a command-line program that displays information about
Internet game servers.

Games supported include Quake, QuakeWorld, Hexen II, Quake II,
HexenWorld, Unreal, Half-Life, Sin, Shogo, Tribes, Tribes 2,
Quake III: Arena, BFRIS, Kingpin, and Heretic II, Unreal Tournament,
Soldier of Fortune, Rogue Spear, Redline, Turok II, Blood 2,
Descent 3, Drakan, KISS, Nerf Arena Blast, Rally Master, Terminous,
Wheel of Time and Daikatana.

Note for Tribes 2: QStat only supports Tribes 2 builds numbered 22075
or higher.

%prep
%setup -q -n %{name}25c

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}
install qstat $RPM_BUILD_ROOT%{_bindir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(0755, root, root)%{_bindir}/qstat
%doc LICENSE.txt CHANGES.txt qstat.cfg contrib.cfg qstatdoc.html template info

Summary:	Game server browsing utility (mostly FPP/FPS)
Summary(pl):	Przegl±darka serwerów gier (g³ównie FPP/FPS)
Name:		qstat
Version:	2.6
Release:	1
License:	Artistic
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/qstat/%{name}-%{version}.tar.gz
# Source0-md5:	68e96ea9dd444ddd7759db02444d398a
URL:		http://www.qstat.org/
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

Note for Tribes 2: qstat only supports Tribes 2 builds numbered 22075
or higher.

%description -l pl
qstat jest dzia³aj±cym z linii poleceñ programem pokazuj±cym
informacje o internetowych serwerach gier.

Posiada on wsparcie m. in. dla gier: Quake, QuakeWorld, Hexen II,
Quake II, HexenWorld, Unreal, Half-Life, Sin, Shogo, Tribes, Tribes 2,
Quake III: Arena, BFRIS, Kingpin, and Heretic II, Unreal Tournament,
Soldier of Fortune, Rogue Spear, Redline, Turok II, Blood 2,
Descent 3, Drakan, KISS, Nerf Arena Blast, Rally Master, Terminous,
Wheel of Time i Daikatana.

Uwaga dotycz±ca Tribes 2: qstat wspiera jedynie Tribes 2 w wersji
(build) 22075 i wy¿szych.

%prep
%setup -q

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
%doc LICENSE.txt CHANGES.txt qstat.cfg contrib.cfg qstatdoc.html template info
%attr(755,root,root) %{_bindir}/qstat

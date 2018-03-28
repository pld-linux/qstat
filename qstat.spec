Summary:	Game server browsing utility (mostly FPP/FPS)
Summary(pl.UTF-8):	Przeglądarka serwerów gier (głównie FPP/FPS)
Name:		qstat
Version:	2.11
Release:	2
License:	Artistic
Group:		Applications/Games
Source0:	http://dl.sourceforge.net/qstat/%{name}-%{version}.tar.gz
# Source0-md5:	26c09831660ef9049fe74b786b80d091
URL:		http://www.qstat.org/
BuildRequires:	autoconf
BuildRequires:	automake
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

%description -l pl.UTF-8
qstat jest działającym z linii poleceń programem pokazującym
informacje o internetowych serwerach gier.

Posiada on wsparcie m. in. dla gier: Quake, QuakeWorld, Hexen II,
Quake II, HexenWorld, Unreal, Half-Life, Sin, Shogo, Tribes, Tribes 2,
Quake III: Arena, BFRIS, Kingpin, and Heretic II, Unreal Tournament,
Soldier of Fortune, Rogue Spear, Redline, Turok II, Blood 2,
Descent 3, Drakan, KISS, Nerf Arena Blast, Rally Master, Terminous,
Wheel of Time i Daikatana.

Uwaga dotycząca Tribes 2: qstat wspiera jedynie Tribes 2 w wersji
(build) 22075 i wyższych.

%prep
%setup -q

%build
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
        DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt CHANGES.txt contrib.cfg qstatdoc.html template/*.{html,txt} info/*.txt
%attr(755,root,root) %{_bindir}/qstat
%{_sysconfdir}/qstat.cfg

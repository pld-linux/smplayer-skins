Summary:	Skins for SMPlayer
Name:		smplayer-skins
Version:	20.11.0
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Multimedia
Source0:	https://downloads.sourceforge.net/smplayer/%{name}-%{version}.tar.bz2
# Source0-md5:	0b2e6aabf497c1248c60c382827d9ba0
URL:		https://www.smplayer.info/
Requires:	smplayer
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Skin themes for SMplayer.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
%{__make}

%{__make} install \
	PREFIX=%{_prefix} \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README.txt Changelog
%{_datadir}/smplayer/themes/Black
%{_datadir}/smplayer/themes/Gonzo
%{_datadir}/smplayer/themes/Mac
%{_datadir}/smplayer/themes/Mint-Y
%{_datadir}/smplayer/themes/Modern
%{_datadir}/smplayer/themes/Vista

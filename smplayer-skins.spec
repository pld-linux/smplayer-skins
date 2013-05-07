Summary:	Skins for SMPlayer
Name:		smplayer-skins
Version:	20121029
Release:	1
License:	GPL v2+
Group:		Applications/Multimedia
Source0:	http://downloads.sourceforge.net/smplayer/%{name}-%{version}.tar.bz2
# Source0-md5:	06ba75b53c7a6e9b64d6f51d05a12a0f
URL:		http://smplayer.sourceforge.net/
Requires:	smplayer
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Skin themes for SMplayer.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
%{__make} \
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
%{_datadir}/smplayer/themes/Modern
%{_datadir}/smplayer/themes/Vista

Summary:	Play with MPlayer the selected video files, and the video files contained inside the selected folders
Name:		nautilus-play-mplayer
Version:	0.1.1
Release:	1
License:	GPL v2
Group:		X11/Libraries
Source0:	http://ppa.launchpad.net/zootropo/ubuntu/pool/main/n/nautilus-play-mplayer/%{name}_%{version}-1.tar.gz
# Source0-md5:	05a5d188382026c6c1bb809de885af50
URL:		http://mundogeek.net/nautilus-scripts/
Patch0:		%{name}-libdir.patch
Requires:	nautilus-python >= 0.4.3
Requires:	python-pygtk >= 2.12.1
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This program adds a new entry to the contextual menu which allows us
to play with MPlayer the selected video files, and the video files
contained inside the selected folders.

%prep
%setup -q
%patch -p1

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	LIBDIR="%{_libdir}" \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc changelog
%{_libdir}/nautilus/extensions-2.0/python/%{name}.py
%{_pixmapsdir}/%{name}.png

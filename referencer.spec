Summary:	Bibliography reference management tool for GNOME
Name:		referencer
Version:	1.1.6
Release:	7
License:	GPLv2
Group:		Graphical desktop/GNOME
URL:		http://icculus.org/referencer/index.html
Source0:	http://icculus.org/referencer/downloads/%{name}-%{version}.tar.gz
# 48x48 PNG from referencer.svg in package, generated with GIMP
Source1:	referencer.png
Patch0:		referencer-1.1.6-poppler-0.16.0.patch

BuildRequires:	desktop-file-utils
BuildRequires:	imagemagick
BuildRequires:	intltool
BuildRequires:	boost-devel
BuildRequires:	pkgconfig(gconfmm-2.6)
BuildRequires:	pkgconfig(gnome-doc-utils)
BuildRequires:	pkgconfig(gnome-vfsmm-2.6)
BuildRequires:	pkgconfig(gtkmm-2.4)
BuildRequires:	pkgconfig(libglademm-2.4)
BuildRequires:	pkgconfig(libgnomeuimm-2.6)
BuildRequires:	pkgconfig(poppler-glib)
BuildRequires:	pkgconfig(python)

%description
Referencer is a GNOME application to organise documents or references, and 
ultimately generate a BibTeX bibliography file.

%prep
%setup -q
%patch0 -p0 -b .poppler

%build
autoreconf -fi
%configure2_5x \
	--disable-scrollkeeper \
	--disable-update-mime-database
%make

%install
%makeinstall_std

# fd.o icons
mkdir -p %{buildroot}%{_iconsdir}/hicolor/{scalable,48x48,32x32,16x16}/apps
install -m 644 %{buildroot}%{_datadir}/pixmaps/%{name}.svg %{buildroot}%{_iconsdir}/hicolor/scalable/apps/%{name}.svg
install -m 644 %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/48x48/apps/%{name}.png
convert -scale 32 %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/32x32/apps/%{name}.png
convert -scale 16 %{SOURCE1} %{buildroot}%{_iconsdir}/hicolor/16x16/apps/%{name}.png

# menu
desktop-file-install --vendor="" \
	--remove-category="Application" \
	--dir %{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/applications/*

%find_lang %{name} --with-gnome --all-name

%files -f %{name}.lang
%doc README AUTHORS ChangeLog TODO
%{_bindir}/%{name}
%{_libdir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}
%{_datadir}/pixmaps/%{name}.svg
%{_datadir}/mime/packages/%{name}.xml
%{_iconsdir}/hicolor/*/apps/%{name}.*
%{_iconsdir}/hicolor/48x48/mimetypes/gnome-mime-application-x-%{name}.png


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



%changelog
* Mon Jun 11 2012 Matthew Dawkins <mattydaw@mandriva.org> 1.1.6-7
+ Revision: 804415
- rebuild for boost libs
- cleaned up spec
- updated poppler patch for newer poppler

* Thu Mar 17 2011 Funda Wang <fwang@mandriva.org> 1.1.6-6
+ Revision: 645787
- rebuild for new boost

* Thu Dec 30 2010 Funda Wang <fwang@mandriva.org> 1.1.6-5mdv2011.0
+ Revision: 626183
- autoreconf
- fix build with poppler 1.16.0
- rebuild for new poppler

* Wed Nov 03 2010 Michael Scherer <misc@mandriva.org> 1.1.6-4mdv2011.0
+ Revision: 592702
- rebuild for python 2.7

* Tue Aug 24 2010 Funda Wang <fwang@mandriva.org> 1.1.6-3mdv2011.0
+ Revision: 572619
- rebuild

* Mon Feb 08 2010 Anssi Hannula <anssi@mandriva.org> 1.1.6-2mdv2011.0
+ Revision: 501882
- rebuild for new boost

* Fri Aug 21 2009 Funda Wang <fwang@mandriva.org> 1.1.6-1mdv2010.0
+ Revision: 418948
- New version 1.1.6
- rebuild for new libboost

* Tue May 19 2009 Götz Waschk <waschk@mandriva.org> 1.1.5-5mdv2010.0
+ Revision: 377495
- rebuild for new poppler

* Thu Mar 26 2009 Funda Wang <fwang@mandriva.org> 1.1.5-4mdv2009.1
+ Revision: 361289
- rebuild for new boost

* Sat Dec 27 2008 Michael Scherer <misc@mandriva.org> 1.1.5-3mdv2009.1
+ Revision: 319918
- rebuild for new python

* Sat Dec 20 2008 Funda Wang <fwang@mandriva.org> 1.1.5-2mdv2009.1
+ Revision: 316578
- rebuild for new boost

  + Oden Eriksson <oeriksson@mandriva.com>
    - lowercase ImageMagick

* Tue Oct 14 2008 Funda Wang <fwang@mandriva.org> 1.1.5-1mdv2009.1
+ Revision: 293456
- BR intltool
- new version 1.1.5
- drop upstream patches

* Thu Sep 25 2008 Frederik Himpe <fhimpe@mandriva.org> 1.1.3-4mdv2009.0
+ Revision: 288220
- Add 2 upstream patches (via Debian) fixing a crash and bibtex
  export

* Tue Aug 19 2008 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.1.3-3mdv2009.0
+ Revision: 273512
- rebuild against new boost

* Fri Aug 08 2008 Thierry Vignaud <tv@mandriva.org> 1.1.3-2mdv2009.0
+ Revision: 269218
- rebuild early 2009.0 package (before pixel changes)

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed May 28 2008 Frederik Himpe <fhimpe@mandriva.org> 1.1.3-1mdv2009.0
+ Revision: 212723
- update to new version 1.1.3

* Thu May 01 2008 Adam Williamson <awilliamson@mandriva.org> 1.1.2-1mdv2009.0
+ Revision: 199865
- new release 1.1.2

* Fri Mar 14 2008 Adam Williamson <awilliamson@mandriva.org> 1.1.1-1mdv2008.1
+ Revision: 187969
- new release 1.1.1

* Sat Mar 01 2008 Adam Williamson <awilliamson@mandriva.org> 1.1.0-1mdv2008.1
+ Revision: 177116
- buildrequires python-devel
- update file list
- correct wrong macro in %%postun
- drop old mdv icons
- fix poppler-glib buildrequire
- drop externally sourced French translation and poppler.patch (both merged upstream)
- minor spec clean
- new release 1.1.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Sun Sep 09 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.4-2mdv2008.0
+ Revision: 82970
- drop X-Mandriva menu category
- Fedora license policy
- add patch0 - from upstream svn, fixes build with poppler 0.6
- add source2 - french translation from Launchpad (Ubuntu)
- spec clean

* Thu May 31 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.4-1mdv2008.0
+ Revision: 33288
- new release 1.0.4

* Mon Apr 30 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.3-2mdv2008.0
+ Revision: 19614
- use --disable-update-mime-database, package reflib type

* Sun Apr 29 2007 Adam Williamson <awilliamson@mandriva.org> 1.0.3-1mdv2008.0
+ Revision: 19326
- create /scalable dir for icon
- 1.0.3; update MIME cache in %%post; generate full icon set


* Mon Mar 05 2007 Adam Williamson <awilliamson@mandriva.com> 1.0.2-2mdv2007.0
+ Revision: 132831
- bump mkrel
- change menu category: fixes 2007 backport, but this is also more correct on Cooker

* Mon Mar 05 2007 Adam Williamson <awilliamson@mandriva.com> 1.0.2-1mdv2007.1
+ Revision: 132825
- fix more BuildRequires
- fix BuildRequires
- work around MIME brokenness
- Import referencer


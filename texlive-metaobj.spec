Name:		texlive-metaobj
Version:	15878
Release:	1
Summary:	MetaPost package providing high-level objects
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/metaobj
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metaobj.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metaobj.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
METAOBJ is a large metapost package providing high-level
objects. It implements many of PSTricks' features for node
connections, but also trees, matrices, and many other things.
It more or less contains boxes.mp and rboxes.mp. There is a
large (albeit not complete) documentation distributed with the
package. It is easily extensible with new objects.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/metapost/metaobj/connections.mp
%{_texmfdistdir}/metapost/metaobj/metaobj.mp
%{_texmfdistdir}/metapost/metaobj/mobjstandard.mp
%{_texmfdistdir}/metapost/metaobj/proofex.mp
%{_texmfdistdir}/metapost/metaobj/pstricksex1.mp
%{_texmfdistdir}/metapost/metaobj/pstricksex2.mp
%{_texmfdistdir}/metapost/metaobj/pstricksex3.mp
%{_texmfdistdir}/metapost/metaobj/pstricksex4.mp
%doc %{_texmfdistdir}/doc/metapost/metaobj/README
%doc %{_texmfdistdir}/doc/metapost/metaobj/license.txt
%doc %{_texmfdistdir}/doc/metapost/metaobj/momanual.pdf

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}

Name:		texlive-metaobj
Version:	0.93
Release:	1
Summary:	MetaPost package providing high-level objects
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/graphics/metapost/contrib/macros/metaobj
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metaobj.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/metaobj.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
METAOBJ is a large metapost package providing high-level
objects. It implements many of PSTricks' features for node
connections, but also trees, matrices, and many other things.
It more or less contains boxes.mp and rboxes.mp. There is a
large (albeit not complete) documentation distributed with the
package. It is easily extensible with new objects.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
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
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar metapost doc %{buildroot}%{_texmfdistdir}

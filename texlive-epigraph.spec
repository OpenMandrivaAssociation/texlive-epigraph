# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/epigraph
# catalog-date 2009-09-02 18:09:14 +0200
# catalog-license lppl1.3
# catalog-version 1.5c
Name:		texlive-epigraph
Version:	1.5c
Release:	5
Summary:	A package for typesetting epigraphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/epigraph
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epigraph.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epigraph.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epigraph.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Epigraphs are the pithy quotations often found at the start (or
end) of a chapter. Both single epigraphs and lists of epigraphs
are catered for. Various aspects are easily configurable.

%post
    %{_sbindir}/texlive.post

%postun
    if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/epigraph/epigraph.sty
%doc %{_texmfdistdir}/doc/latex/epigraph/README
%doc %{_texmfdistdir}/doc/latex/epigraph/epigraph.pdf
#- source
%doc %{_texmfdistdir}/source/latex/epigraph/epigraph.dtx
%doc %{_texmfdistdir}/source/latex/epigraph/epigraph.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.5c-2
+ Revision: 751493
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.5c-1
+ Revision: 718344
- texlive-epigraph
- texlive-epigraph
- texlive-epigraph
- texlive-epigraph


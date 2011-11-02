Name:		texlive-epigraph
Version:	1.5c
Release:	1
Summary:	A package for typesetting epigraphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/epigraph
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epigraph.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epigraph.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epigraph.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
Epigraphs are the pithy quotations often found at the start (or
end) of a chapter. Both single epigraphs and lists of epigraphs
are catered for. Various aspects are easily configurable.

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

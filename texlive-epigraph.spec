Name:		texlive-epigraph
Version:	54857
Release:	1
Summary:	A package for typesetting epigraphs
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/epigraph
License:	LPPL1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epigraph.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epigraph.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/epigraph.source.r%{version}.tar.xz
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
%{_texmfdistdir}/tex/latex/epigraph
%doc %{_texmfdistdir}/doc/latex/epigraph
#- source
%doc %{_texmfdistdir}/source/latex/epigraph

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}

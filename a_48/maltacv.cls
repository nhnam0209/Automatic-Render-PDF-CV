%%%%%%%%%%%%%%%%%
% This is altacv.cls (v1.1.5, 1 December 2018) written by
% LianTze Lim (liantze@gmail.com).
%
%% It may be distributed and/or modified under the
%% conditions of the LaTeX Project Public License, either version 1.3
%% of this license or (at your option) any later version.
%% The latest version of this license is in
%%    http://www.latex-project.org/lppl.txt
%% and version 1.3 or later is part of all distributions of LaTeX
%% version 2003/12/01 or later.
%%
%%
% Contributions:
% - https://github.com/akreuzer Added ragged2e option (5 Nov 2018)
% - https://github.com/stefanogermano Fixed bad boxes and undefined font shape (July 2018)
% - https://github.com/foohyfooh Fixed blank spaces in \cvevent and bad link in README.md (June 2018)

%%%%%%%%%%%%%%%%
\NeedsTeXFormat{LaTeX2e}[1995/12/01]
%% v1.4: Detect TL2018 to handle accented characters in class information
\@ifl@t@r\fmtversion{2018/04/01}{\UseRawInputEncoding}{}
\ProvidesClass{maltacv}[2018/12/01 MAltaCV v1.1.5, yet another alternative class for a résumé/curriculum vitae.]

%% v1.1: Optionally load academicons
\newif\if@academicons
\DeclareOption{academicons}{\@academiconstrue}
%% v1.1.3: Choice of round/square photo
\newif\if@normalphoto
\DeclareOption{normalphoto}{\@normalphototrue}
\DeclareOption*{\PassOptionsToClass{\CurrentOption}{extarticle}}
\newif\if@raggedtwoe
\DeclareOption{ragged2e}{\@raggedtwoetrue}
\ProcessOptions\relax

\LoadClass{extarticle}

\RequirePackage[margin=1cm]{geometry}
\RequirePackage{fontawesome}
\RequirePackage{ifxetex,ifluatex}
\RequirePackage{scrlfile}

%% v1.1.5: added for convenience
\newif\ifxetexorluatex
\ifxetex
  \xetexorluatextrue
\else
  \ifluatex
    \xetexorluatextrue
  \else
    \xetexorluatexfalse
  \fi
\fi

%% v1.1: Optionally load academicons
%% v1.1.5: Handle different versions of academicons
\if@academicons
  \ifxetexorluatex
    \RequirePackage{fontspec}
    %% academicons in TL2018 doesn't require
    %% Academicons to be installed in OS fonts
    %% so can be loaded directly
    \@ifl@t@r\fmtversion{2018/04/01}{%
      \RequirePackage{academicons}
    }{%
      % TL2017
      \@ifl@t@r\fmtversion{2017/04/01}{%
        \@ifpackagelater{academicons}{2018/03/01}{%
          \RequirePackage{academicons}
        }{%
          \let\ori@newfontfamily\newfontfamily%
          \renewcommand{\newfontfamily}[2]{}
          \RequirePackage{academicons}
          \let\newfontfamily\ori@newfontfamily
          \newfontfamily{\AI}{academicons.ttf}
        }
      }{% TL2016 requires the package to be loaded before
        % the version can be checked. Only added because
        % Overleaf v1 still runs TL2016; will be removed
        % when v1 is completely retired.
          \let\ori@newfontfamily\newfontfamily%
          \renewcommand{\newfontfamily}[2]{}
          \RequirePackage{academicons}
          \let\newfontfamily\ori@newfontfamily
          \newfontfamily{\AI}{academicons.ttf}
      }
    }
  \else
    \ClassError{AltaCV}{academicons unsupported by latex or pdflatex. Please compile with xelatex or lualatex}{Please compile with xelatex or lualatex to use the academicons option}
  \fi
\fi

\if@raggedtwoe
  \RequirePackage[newcommands]{ragged2e}
\fi

\RequirePackage{xcolor}
\RequirePackage{pdftexcmds}

% Original blue as default
\definecolor{Body}{HTML}{000000}
\definecolor{SecondaryBody}{HTML}{333333}
\definecolor{LightBody}{HTML}{ffffff}
\definecolor{LightIcons}{HTML}{ffffff}
\definecolor{AccentBody}{HTML}{002256}
\definecolor{Primary}{HTML}{27507d}

\colorlet{primary}{Primary}
\colorlet{accent_body}{AccentBody}
\colorlet{body}{Body}
\colorlet{secondary_body}{SecondaryBody}
\colorlet{light_body}{LightBody}
\colorlet{light_icons}{LightIcons}
\newcommand{\itemmarker}{{\small\textbullet}}
\newcommand{\ratingmarker}{\faCircle}

\newcommand{\setcolorscheme}[1]{
  \stringcases
    {#1}
    {
      {raisinblack_flame}{
        % Coolcolors raisin black + flame
        \definecolor{AccentBody}{HTML}{2E282A}
        \definecolor{Primary}{HTML}{E4572E}
      }
      {darkpurple_princetonorange}{
        % Coolcolors dark purple + princeton orange
        \definecolor{AccentBody}{HTML}{291720}
        \definecolor{Primary}{HTML}{E87D20}
      }
      {blue_claret}{
        % Coolcolors prussian blue + claret
        \definecolor{AccentBody}{HTML}{002642}
        \definecolor{Primary}{HTML}{840032}
      }
      {eerieblack_eggplant}{
        % Coolcolors eerie black + eggplant
        \definecolor{AccentBody}{HTML}{141115}
        \definecolor{Primary}{HTML}{4C2B36}
      }
      {outerspace_forestgreen}{        
        % Coolcolors outer space + forest green
        \definecolor{AccentBody}{HTML}{2D3A3A}
        \definecolor{Primary}{HTML}{248232}
      }
      {raisinblack_midnightgreen}{
        % Coolcolors raisin black + midnight green
        \definecolor{AccentBody}{HTML}{28262C}
        \definecolor{Primary}{HTML}{225560}
      }
      {teal_brown}{
        % Coolcolors teal + brown
        \definecolor{AccentBody}{HTML}{3A2E39}
        \definecolor{Primary}{HTML}{1E555C}
      }
      {indigo}{
        % Material indigo
        \definecolor{AccentBody}{HTML}{1A237E}
        \definecolor{Primary}{HTML}{303F9F}
      }
      {blue}{
        % Original blue
        \definecolor{AccentBody}{HTML}{002256}
        \definecolor{Primary}{HTML}{27507d}
      }
      {violet}{
        % Coolcolors violet
        \definecolor{Primary}{HTML}{4b506d}
        \definecolor{AccentBody}{HTML}{0B132B}
      }
    }
    {[nada]}
  \colorlet{primary}{Primary}
  \colorlet{accent_body}{AccentBody}
}

% Helper functions to create the switch case above
\newcommand{\stringcases}[3]{%
  \romannumeral
  \str@case{#1}#2{#1}{#3}\q@stop
}
\newcommand{\str@case}[3]{%
  \ifnum\pdf@strcmp{\unexpanded{#1}}{\unexpanded{#2}}=\z@
    \expandafter\@firstoftwo
  \else
    \expandafter\@secondoftwo
  \fi
  {\str@case@end{#3}}
  {\str@case{#1}}%
}
\newcommand{\str@case@end}{}
\long\def\str@case@end#1#2\q@stop{\z@#1}
  
\RequirePackage{tikz}
\usetikzlibrary{arrows}
\RequirePackage[skins]{tcolorbox}
\RequirePackage{enumitem}
\setlist{leftmargin=*,labelsep=0.5em,nosep,itemsep=0pt}
\setlist[itemize]{label=\itemmarker}
\RequirePackage{graphicx}
\RequirePackage{etoolbox}
\RequirePackage{dashrule}
\RequirePackage{multirow,tabularx}
\RequirePackage{changepage}
\RequirePackage{tcolorbox}
% \RequirePackage{marginfix}

\newtcolorbox{section_box}{colback=accent_body,colframe=accent_body,
boxrule=2pt,arc=0pt,boxsep=2pt,left=3pt,right=3pt,top=3pt,bottom=3pt,leftrule=0pt}

\newtcolorbox{subsection_box}{colback=white,colframe=accent_body,
boxrule=2pt,arc=0pt,boxsep=2pt,left=2pt,right=2pt,top=2pt,bottom=2pt}

\setlength{\parindent}{0pt}
\newcommand{\divider}{\medskip}

\newcommand{\emailsymbol}{\faAt}
\newcommand{\phonesymbol}{\faPhone}
\newcommand{\homepagesymbol}{\faChain}
\newcommand{\locationsymbol}{\faMapMarker}
\newcommand{\linkedinsymbol}{\faLinkedin}
\newcommand{\twittersymbol}{\faTwitter}
\newcommand{\githubsymbol}{\faGithub}
\newcommand{\facebooksymbol}{\faFacebook}
\newcommand{\mailsymbol}{\faEnvelope}
\newcommand{\birthdaysymbol}{\faBirthdayCake}

\newcommand{\printinfo}[2]{\mbox{\makebox[1.5em][c]{\textcolor{light_icons}{\normalfont #1}}\hspace{0.5em}\textcolor{light_body}{#2}\hspace{2em}}}

\newcommand{\name}[1]{\def\@name{#1}}
\newcommand{\firstname}[1]{\def\@firstname{#1}}
\newcommand{\familyname}[1]{\def\@familyname{#1}}
\newcommand{\tagline}[1]{\def\@tagline{#1}}
\newcommand{\email}[1]{\href{mailto:#1}{\printinfo{\emailsymbol}{#1}}}
\newcommand{\mailaddress}[1]{\printinfo{\mailsymbol}{#1}}
\newcommand{\phone}[1]{\printinfo{\phonesymbol}{#1}}
\newcommand{\homepage}[1]{\href{https://#1}{\printinfo{\homepagesymbol}{#1}}}
\newcommand{\twitter}[1]{\printinfo{\twittersymbol}{#1}}
\newcommand{\linkedin}[1]{\href{https://www.linkedin.com/in/#1}{\printinfo{\linkedinsymbol}{#1}}}
\newcommand{\github}[1]{\href{https://www.github.com/#1}{\printinfo{\githubsymbol}{#1}}}
\newcommand{\facebook}[1]{\href{https://www.facebook.com/#1}{\printinfo{\facebooksymbol}{#1}}}
\newcommand{\location}[1]{\printinfo{\locationsymbol}{#1}}
\newcommand{\birthday}[1]{\printinfo{\birthdaysymbol}{#1}}

\newcommand{\personalinfo}[1]{\def\@personalinfo{#1}}

\newcommand{\bio}[1]{\def\@bio{#1}}

\newcommand{\namefont}{\bfseries\fontsize{24}{24}\mdseries}

\newcommand{\makecvheader}{%
  \begingroup
    \raggedright\color{accent_body}%
    {\namefont{\color{accent_body}\@firstname} {\color{accent_body}\@familyname}\par}
    \medskip
    {\large\itshape\color{secondary_body}\@tagline\par}

    \ifstrequal{\@bio}{}{}{
      \medskip
      \color{secondary_body}\@bio\par
    }


    \medskip

    \noindent\makebox[\textwidth][l]{%
      \hspace{-\dimexpr\oddsidemargin+1in}%
      \colorbox{primary}{%
        \parbox{\dimexpr\paperwidth-6\fboxsep}{
          \vspace*{-\medskipamount}
          \center\color{light_body}\@personalinfo\par
          \smallskip
        }%
      }%
    }

  \endgroup\medskip
}

\newcommand{\cvsection}[2][]{%
  \medskip
  {\Large\color{primary}\bfseries\MakeUppercase{#2}}\\[-1ex]%
  \medskip\color{body}
}

\newcommand{\cvsubsection}[1]{%
  \medskip%
  {\large\color{accent_body}\bfseries\MakeUppercase{#1}}\\[-1ex]%
  % {\color{emphasis}\rule{\linewidth}{1pt}\par}\medskip
  \medskip\color{body}
}

\newcommand{\cvsubsubsection}[1]{%
  \smallskip%
  {\color{primary}\bfseries\MakeUppercase{#1}\par}\smallskip
}

% v1.1.4: fixes inconsistent font size
\newcommand{\cvevent}[3]{%
  \smallskip
  {\large\color{accent_body}\textbf{#1}\par}
  \smallskip
  \ifstrequal{#2}{}{}{{\color{secondary_body}\small{\faCalendar\hspace{0.5em}#2}}\hspace{1em}}\par
  \ifstrequal{#3}{}{}{{\color{secondary_body}\small{\faBuilding\hspace{0.5em}#3}}\hspace{1em}}\par
  \smallskip\normalsize\color{body}
}
% v1.1.4: fixes inconsistent font size
\newcommand{\cvuniversity}[5]{%
  \smallskip
  {\large\color{accent_body}\textbf{#1}\par}
  \smallskip
  \ifstrequal{#2}{}{}{{\color{secondary_body}\small{\faCertificate\hspace{0.5em}#2}}\hspace{1em}}
  \ifstrequal{#3}{}{}{{\color{secondary_body}\small{\faCalendar\hspace{0.5em}#3}}\hspace{1em}}\par
  \ifstrequal{#4}{}{}{{\color{secondary_body}\small{\faUniversity\hspace{0.5em}#4}}\hspace{1em}}\par
    \ifstrequal{#5}{}{}{{\color{secondary_body}\small{\faGraduationCap\hspace{0.5em}#5}}\hspace{1em}}\par
  \smallskip\normalsize\color{body}
}

% v1.1.4: fixes inconsistent font size
\newcommand{\cvexperience}[4]{%
  \smallskip
  {\large\color{accent_body}\textbf{#1}\par}
  \smallskip
  \ifstrequal{#2}{}{}{{\color{secondary_body}\small{\faBuilding\hspace{0.5em}#2}}\hspace{1em}}\par
  \ifstrequal{#3}{}{}{{\color{secondary_body}\small{\faCalendar\hspace{0.5em}#3}}\hspace{1em}}\par
  \ifstrequal{#4}{}{}{{\color{secondary_body}\small{\faMapMarker\hspace{0.5em}#4}}\hspace{1em}}\par
  \smallskip\normalsize\color{body}
}

\newcommand{\cvproject}[2]{%
  \smallskip
  {\large\color{accent_body}\textbf{#1}\par}
  \smallskip
  \ifstrequal{#2}{}{}{{\color{secondary_body}\small{\faCalendar\hspace{0.5em}#2}}\hspace{1em}}\par
  \smallskip\normalsize\color{body}
}

\newcommand{\cvlistitem}[2]{%
{\bfseries\color{accent_body}{#1}}\\
\ifstrequal{#2}{}{}{\itshape\color{secondary_body}{#2}}\color{body}\par
\medskip
}

\newenvironment{cvcolumn}[1]{\begin{minipage}[t]{#1}\raggedright}{\end{minipage}}

\RequirePackage[backend=biber,style=authoryear,sorting=ydnt]{biblatex}
%% For removing numbering entirely when using a numeric style
% \setlength{\bibhang}{1em}
% \DeclareFieldFormat{labelnumberwidth}{\makebox[\bibhang][l]{\itemmarker}}
% \setlength{\biblabelsep}{0pt}
\defbibheading{pubtype}{\cvsubsection{#1}}
\renewcommand{\bibsetup}{\vspace*{-\baselineskip}}
\AtEveryBibitem{\makebox[\bibhang][l]{\itemmarker}}
\setlength{\bibitemsep}{0.25\baselineskip}

% v1.1.2: make it easier to add a sidebar aligned with top of next page
\RequirePackage{afterpage}
\newcommand{\addsidebar}[2][]{\marginpar{%
  \ifstrequal{#1}{}{}{\vspace*{#1}}%
  \input{#2}}%
}
\newcommand{\addnextpagesidebar}[2][]{\afterpage{\addsidebar[#1]{#2}}}

\AtBeginDocument{%
  \pagestyle{empty}
  \color{body}
  \raggedright
}

\AtEndPreamble{
  \RequirePackage[unicode]{hyperref}% unicode is required for unicode pdf metadata
  \hypersetup{
    breaklinks,
    baseurl       = http://,
    pdfborder     = 0 0 0,
    pdfpagemode   = UseNone,% do not show thumbnails or bookmarks on opening
    pdfstartpage  = 1,
    pdfcreator    = {\LaTeX{} with tweaked 'AltoCV' style },
%    pdfproducer   = {\LaTeX{}},% will/should be set automatically to the correct TeX engine used
    bookmarksopen = false,
    bookmarksdepth= 2,% to show sections and subsections
    pdfauthor     = {\@firstname{}~\@familyname{}},
    pdftitle      = {\@firstname{}~\@familyname{} - CV},
    pdfsubject    = {Curriculum Vit\ae of \@firstname{}~\@familyname{}},
    pdfkeywords   = {\@firstname{}~\@familyname{}, curriculum vit\ae{}, resum\'{e}}}
}

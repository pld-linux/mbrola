Summary:	MBROLA is a speech synthesizer based on the concatenation of diphones
Summary(pl):	MBROLA to syntezator mowy bazuj±cy na ³±czeniu dwuzg³osek
Name:		mbrola
Version:	301h
Release:	1
License:	Non-commercial, non-military purposes, w/ and only w/ the voice and language databases available on http://tcts.fpms.ac.be/synthesis
Group:		Applications/Sound
Source0:	http://tcts.fpms.ac.be/synthesis/mbrola/bin/pclinux/mbr%{version}.zip
Source1:	http://tcts.fpms.ac.be/synthesis/mbrola/dba/us1/us1-980512.zip
Source2:	http://tcts.fpms.ac.be/synthesis/mbrola/dba/us2/us2-980812.zip
Source3:	http://tcts.fpms.ac.be/synthesis/mbrola/dba/us3/us3-990208.zip
Source4:	http://tcts.fpms.ac.be/synthesis/mbrola/dba/en1/en1-980910.zip
Source5:	http://tcts.fpms.ac.be/synthesis/mbrola/dba/pl1/pl1.zip
URL:		http://tcts.fpms.ac.be/synthesis/mbrola.html
ExclusiveArch:	%{ix86} ppc alpha
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
MBROLA is a speech synthesizer based on the concatenation of diphones.
It takes a list of phonemes as input, together with prosodic
information (duration of phonemes and a piecewise linear description
of pitch), and produces speech samples on 16 bits (linear), at the
sampling frequency of the diphone database.

It is therefore NOT a Text-To-Speech (TTS) synthesizer, since it does
not accept raw text as input. In order to obtain a full TTS system,
you need to use this synthesizer in combination with a text processing
system that produces phonetic and prosodic commands.

%description -l pl
MBROLA jest syntezatorem mowy opartym o po³±czenia dwuzg³osek. Jako
dane wej¶ciowe pobiera listê fonemów, ³±cznie z informacj± prozodyczn±
(d³ugo¶æ fonemów oraz cz±stkowy liniowy opis tonacji), po czym tworzy
16-bitowe (liniowe) próbki mowy o czêstotliwo¶ci próbkowania pobranej
z bazy dwuzg³osek.

NIE jest to syntezator przetwarzaj±cy tekst na mowê (Text-To-Speech,
TTS), gdy¿ nie przyjmuje jako danych wej¶ciowych czystego tekstu. Aby
uzyskaæ pe³ny system TTS trzeba pos³ugiwaæ siê tym syntezatorem
³±cznie z systemem przetwarzania tekstu, który tworzy polecenia
fonetyczno-prozodyczne jako dane wynikowe.

%package voice-us1
Summary:	Files for voice us1 to be used w/ festival
Summary(pl):	Pliki do g³osu us1 przeznaczone dla festival
Group:		Applications/Sound
Requires:	%{name}

%description voice-us1
Files for voice us1 to be used w/ festival.

%description voice-us1 -l pl
Pliki do g³osu us1 przeznaczone dla festival.

%package voice-us2
Summary:	Files for voice us2 to be used w/ festival
Summary(pl):	Pliki do g³osu us2 przeznaczone dla festival
Group:		Applications/Sound
Requires:	%{name}

%description voice-us2
Files for voice us2 to be used w/ festival.

%description voice-us2 -l pl
Pliki do g³osu us2 przeznaczone dla festival.

%package voice-us3
Summary:	Files for voice us3 to be used w/ festival
Summary(pl):	Pliki do g³osu us3 przeznaczone dla festival
Group:		Applications/Sound
Requires:	%{name}

%description voice-us3
Files for voice us3 to be used w/ festival.

%description voice-us3 -l pl
Pliki do g³osu us3 przeznaczone dla festival.

%package voice-en1
Summary:	Files for voice en1 to be used w/ festival
Summary(pl):	Pliki do g³osu en1 przeznaczone dla festival
Group:		Applications/Sound
Requires:	%{name}

%description voice-en1
Files for voice en1 to be used w/ festival.

%description voice-en1 -l pl
Pliki do g³osu en1 przeznaczone dla festival.

%package voice-pl1
Summary:	Files for voice pl1 to be used w/ festival
Summary(pl):	Pliki do g³osu pl1 przeznaczone dla festival
Group:		Applications/Sound
Requires:	%{name}

%description voice-pl1
Files for voice pl1 to be used w/ festival.

%description voice-pl1 -l pl
Pliki do g³osu pl1 przeznaczone dla festival.

%prep
%setup -q -c %{name} -a1 -a2 -a3 -a4 -a5 -c pl

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_bindir},%{_datadir}/festival/lib/voices/{english/{us{1,2,3},en1}_mbrola/{us{1,2,3},en1},polish/pl1_mbrola/pl1}}

%ifarch %{ix86}
install mbrola-linux-i386	$RPM_BUILD_ROOT%{_bindir}/mbrola
%endif
%ifarch ppc
install mbrola206a-linux-ppc	$RPM_BUILD_ROOT%{_bindir}/mbrola
%endif
%ifarch alpha
install mbrola-linux-alpha	$RPM_BUILD_ROOT%{_bindir}/mbrola
%endif
# there is sparc binary also

install us1/us1{,mrpa} $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/english/us1_mbrola/us1/
install us2/us2 $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/english/us2_mbrola/us2/
install us3/us3 $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/english/us3_mbrola/us3/
install en1/en1{,mrpa} $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/english/en1_mbrola/en1/
install pl1 $RPM_BUILD_ROOT%{_datadir}/festival/lib/voices/polish/pl1_mbrola/pl1/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/*
%doc readme.txt

%files voice-us1
%defattr(644,root,root,755)
%doc us1/license.txt us1/us1.txt
%doc %dir us1/TEST
%dir %{_datadir}/festival/lib/voices/english/us1_mbrola
%{_datadir}/festival/lib/voices/english/us1_mbrola/us1

%files voice-us2
%defattr(644,root,root,755)
%doc us2/license.txt us2/us2.txt
%doc %dir us2/TEST
%dir %{_datadir}/festival/lib/voices/english/us2_mbrola
%{_datadir}/festival/lib/voices/english/us2_mbrola/us2

%files voice-us3
%defattr(644,root,root,755)
%doc us3/license.txt us3/us3.txt
%doc %dir us3/TEST
%dir %{_datadir}/festival/lib/voices/english/us3_mbrola
%{_datadir}/festival/lib/voices/english/us3_mbrola/us3

%files voice-en1
%defattr(644,root,root,755)
%doc en1/en1.txt
%doc %dir en1/TEST
%dir %{_datadir}/festival/lib/voices/english/en1_mbrola
%{_datadir}/festival/lib/voices/english/en1_mbrola/en1

%files voice-pl1
%defattr(644,root,root,755)
%doc pl1.txt license.txt
%doc %dir test
%dir %{_datadir}/festival/lib/voices/polish/pl1_mbrola
%{_datadir}/festival/lib/voices/polish/pl1_mbrola/pl1

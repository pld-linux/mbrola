Summary:	MBROLA is a speech synthesizer based on the concatenation of diphones
Summary(pl):	MBROLA to syntezator mowy bazuj�cy na ��czeniu dwuzg�osek
Name:		mbrola
Version:	301h?
Release:	1
License:	Non-commercial, non-military purposes, w/ and only w/ the voice and language databases available on http://tcts.fpms.ac.be/synthesis
Group:		Applications/Sound
Source0:	http://tcts.fpms.ac.be/synthesis/mbrola/bin/pclinux/mbr301h.zip
Source1:	http://tcts.fpms.ac.be/synthesis/mbrola/dba/us1/us1-980512.zip
Source2:	http://tcts.fpms.ac.be/synthesis/mbrola/dba/us2/us2-980812.zip
Source3:	http://tcts.fpms.ac.be/synthesis/mbrola/dba/us3/us3-990208.zip
Source4:	http://tcts.fpms.ac.be/synthesis/mbrola/dba/en1/en1-980910.zip
Source5:	http://tcts.fpms.ac.be/synthesis/mbrola/dba/pl1/pl1.zip
URL:		http://tcts.fpms.ac.be/synthesis/mbrola.html

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
MBROLA jest syntezatorem mowy opartym o po��czenia dwuzg�osek. Jako
dane wej�ciowe pobiera list� fonem�w, ��cznie z informacj� prozodyczn�
(d�ugo�� fonem�w oraz cz�stkowy liniowy opis tonacji), po czym tworzy
16-bitowe (liniowe) pr�bki mowy o cz�stotliwo�ci pr�bkowania pobranej
z bazy dwuzg�osek.

NIE jest to syntezator przetwarzaj�cy tekst na mow� (Text-To-Speech,
TTS), gdy� nie przyjmuje jako danych wej�ciowych czystego tekstu. Aby
uzyska� pe�ny system TTS trzeba pos�ugiwa� si� tym syntezatorem
��cznie z systemem przetwarzania tekstu, kt�ry tworzy polecenia
fonetyczno-prozodyczne jako dane wynikowe.

%package voice-us1
Summary:	Files for voice us1 to be used w/ festival
Summary(pl):	Pliki do g�osu us1 przeznaczone dla festival
Group:		Applications/Sound

%description voice-us1

%description voice-us1 -l pl

%prep

%install

rm -rf $RPM_BUILD_ROOT
%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc readme.txt

%files voice-us1
%defattr(644,root,root,755)
%{_datadir}/

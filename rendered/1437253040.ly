% 2015-07-18 13:57

\version "2.18.2"
\language "english"

\header {
    tagline = \markup {}
}

\layout {}

\paper {}

\score {
    \new Score <<
        \tempo 4=240
        \new Staff {
            {
                g'4
                f'4
                a'4
                f''4
                a'4
                g''4
                f''4
                d''4
                a'4
                d'4
                a'4
                f''4
                f''4
                c''4
                c''4
                d'4
                f''4
                c''4
                d'4
                g'4
            }
        }
        \new Staff {
            {
                d'4
                d'4
                f'4
                d'4
                c''4
                g''4
                d'4
                g'4
                g''4
                bf'4
                f''4
                c''4
                g'4
                d'4
                bf'4
                d'4
                bf'4
                g'4
                d'4
                f'4
            }
        }
    >>
}
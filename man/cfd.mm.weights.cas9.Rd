% Generated by roxygen2: do not edit by hand
% Please edit documentation in R/data.R
\docType{data}
\name{cfd.mm.weights.cas9}
\alias{cfd.mm.weights.cas9}
\title{Mismatch position weights for the CFD off-target algorithm (Cas9)}
\format{
Numeric vector
}
\source{
\url{https://dx.doi.org/10.1038\%2Fnbt.3437}
}
\usage{
cfd.mm.weights.cas9
}
\description{
CFD off-target scoring weights for each nucleotide position and each
    pair of DNA:RNA mismatches, for 20-mer spacer sequences.
    Position 20 refers to the spacer position adjacent to
    the PAM sequence. A higher weight indicates greater mismatch tolerance 
    by the Cas9 nuclease.
}
\keyword{datasets}

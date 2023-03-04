# Missalettes for Masses at St. Joseph's Catholic Church, Gateshead

This repository holds source code to generate missalettes for Masses at
St. Joseph's Catholic Church, Gateshead.  Masses are generated with a copier
template, such as [MassTemplate](https://github.com/2e0byo/MassTemplate).

## Getting pdfs

Pdfs should built automatically and deployed to the
[latest release](https://github.com/St-Josephs-Gateshead/Masses/releases).

## Adding a mass

Clone/fork this repository, make an appropriate directory, and use copier, e.g.:

```shell
cd /path/to/repo
mkdir new-mass # do pick a good name...
copier copy gh:2e0byo/MassTemplate.git new-mass
```

Then edit `propers.tex` and add the required `.gabc` files, e.g. from
[gregobase](https://gregobase.selapa.net).

Later on you may wish to pull in updates from the template.  Assuming you have
committed your changes, run `copier update` from within the directory.  It is
best to overwrite everything, and then use `git diff` / `magit` / your favourite
git frontend to see what changes to discard and what to keep.

## Building locally

The templates will drop a Makefile into the directory.  If you wish to build
everything locally, like the ci does, have a look at `scripts/configure.py`.
(This relies on github actions variables, so it won't currently run locally, but
it's trivial to hard code the url to fetch the latest release.)

## Fast CI

Building gregoriotex documents takes *for ever*.  Most pushes only update one or
two Masses, but as the repository grows we grind to a halt trying to rebuild
everything.

The solution is to rely on document versioning to see when we need to update a
pdf.  Since we upload a snapshot of the sourcecode when we make a release, we
can compare the version number at the time of last release with the version
number now.  If they are unchanged and a pdf exists in the release, we pull in
the pdf and move on; otherwise we mark the directory as needing rebuilding.
Lastly we generate a makefile for all directories in need of work.

Although this is recursive make, it's actually fine in this case: `make` just
calls `latexmk`, and the number of jobs is roughly equivalent to the number of
directories, so the only loss we have is not building the pew sheet in parallel
with the booklet, which is generally trivial.

Note that we deliberately rely on version numbers rather than diffs.  If you do
not bump the version number, no release will happen.  This forces changed pdfs
to have different version numbers.

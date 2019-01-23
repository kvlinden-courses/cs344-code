% The Black Family Tree
% (modified from http://en.wikibooks.org/wiki/Prolog/Introduction/Answers)
%
% author:  kvlinden
% version: Spring, 2013

man(sirius_black).
man(regulus_black).
man(orion_black).
man(cygnus_black).
man(pollux_black).

woman(bellatrix_black).
woman(andromeda_black).
woman(narcissa_black).
woman(walburga_black).
woman(druella_roisier).
woman(irma_crabbe).

parents(lucius_malfoy, narcissa_black, draco_malfoy).
parents(orion_black, walburga_black, sirius_black).
parents(orion_black, walburga_black, regulus_black).
parents(cygnus_black, druella_roisier, bellatrix_black).
parents(cygnus_black, druella_roisier, andromeda_black).
parents(cygnus_black, druella_roisier, narcissa_black).
parents(pollux_black, irma_crabbe, walburga_black).
parents(pollux_black, irma_crabbe, cygnus_black).

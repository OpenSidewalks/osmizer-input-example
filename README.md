# Osmizer-input-example

Example code for preparing data for the
[osmizer](https://github.com/OpenSidewalks/osmizer) command line application.

## Installation

1. Clone this repository
    git clone https://github.com/OpenSidewalks/osmizer-input-example
2. Install the required packages using `pip`:
    pip install -r requirements.txt

## Running the code

    python convert.py

`convert.py` reads the files in the input directory and converts them to a
GeoJSON format that is compatible with `osmizer`. The input files, in this
case, originate from http://accessmapseattle.com and are derived from the
Seattle sidewalk dataset at http://data.seattle.gov. The original municipal
data encodes information like curb ramps as labels on sidewalks and has no
crossing information, so these were generated in previous work ([SSG 2015
Sidewalks group](http://uwescience.github.io/DSSG_sidewalk/2015/08/28/Sidewalks-Project-Summary.html)).

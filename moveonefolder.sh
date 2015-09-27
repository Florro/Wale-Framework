mkdir allheads;
find heads -name '*.jpg' -exec mv {} allheads \;
find jeanheads -name '*.jpg' -exec mv {} allheads \;
rmdir jeanheads;
rmdir heads;

#!/usr/bin/env python
for i in range(len(review)):
    review[i]=review[i].replace("&#8217;","'")
    review[i]=review[i].replace("&#8220;","'")
    review[i]=review[i].replace("&#8221;","'")
    review[i]=review[i].replace("#8230;","...")
    

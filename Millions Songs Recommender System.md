
### Import Graphlab


```python
import sys
sys.path
sys.path.append('/Users/oindrilasen/anaconda/envs/gl-env/lib/python2.7/site-packages')
import graphlab
```

### Load Data


```python
songs = graphlab.SFrame.read_csv("https://static.turi.com/datasets/millionsong/song_data.csv")
usage_data = graphlab.SFrame.read_csv("https://static.turi.com/datasets/millionsong/10000.txt",
                                header=False,
                                delimiter='\t',
                                column_type_hints={'X3':int})
```


<pre>Finished parsing file https://static.turi.com/datasets/millionsong/song_data.csv</pre>



<pre>Parsing completed. Parsed 100 lines in 2.42631 secs.</pre>


    ------------------------------------------------------
    Inferred types from first 100 line(s) of file as 
    column_type_hints=[str,str,str,str,int]
    If parsing fails due to incorrect types, you can correct
    the inferred type list above and pass it to read_csv in
    the column_type_hints argument
    ------------------------------------------------------



<pre>Read 637410 lines. Lines per second: 237212</pre>



<pre>Finished parsing file https://static.turi.com/datasets/millionsong/song_data.csv</pre>



<pre>Parsing completed. Parsed 1000000 lines in 3.31717 secs.</pre>



<pre>Finished parsing file https://static.turi.com/datasets/millionsong/10000.txt</pre>



<pre>Parsing completed. Parsed 100 lines in 1.88218 secs.</pre>



<pre>Read 844838 lines. Lines per second: 391575</pre>



<pre>Finished parsing file https://static.turi.com/datasets/millionsong/10000.txt</pre>



<pre>Parsing completed. Parsed 2000000 lines in 3.07051 secs.</pre>


## 2. Explore Data


```python
len(songs)
```




    1000000




```python
songs
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">song_id</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">title</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">release</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">artist_name</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">year</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOQMMHC12AB0180CB8</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Silent Night</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Monster Ballads X-Mas</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Faster Pussy cat</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2003</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOVFVAK12A8C1350D9</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Tanssi vaan</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Karkuteillä</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Karkkiautomaatti</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1995</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOGTUKN12AB017F4F1</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">No One Could Ever</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Butter</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Hudson Mohawke</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2006</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOBNYVR12A8C13558C</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Si Vos Querés</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">De Culo</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Yerba Brava</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2003</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOHSBXH12A8C13B0DF</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Tangle Of Aspens</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Rene Ablaze Presents<br>Winter Sessions ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Der Mystic</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOZVAPQ12A8C13B63C</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Symphony No. 1 G minor<br>"Sinfonie ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Berwald: Symphonies Nos.<br>1/2/3/4 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">David Montgomery</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOQVRHI12A6D4FB2D7</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">We Have Got Love</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Strictly The Best Vol. 34</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Sasha / Turbulence</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOEYRFT12AB018936C</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2 Da Beat Ch'yall</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Da Bomb</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Kris Kross</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1993</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOPMIYT12A6D4F851E</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Goodbye</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Danny Boy</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Joseph Locke</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOJCFMH12A8C13B0C2</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Mama_ mama can't you see<br>? ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">March to cadence with the<br>US marines ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">The Sun Harbor's Chorus-<br>Documentary Recordings ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0</td>
    </tr>
</table>
[1000000 rows x 5 columns]<br/>Note: Only the head of the SFrame is printed.<br/>You can use print_rows(num_rows=m, num_columns=n) to print more rows and columns.
</div>




```python
len(usage_data)
```




    2000000




```python
usage_data
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">X1</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">X2</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">X3</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOAKIMP12A8C130995</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOBBMDR12A8C13253B</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOBXHDL12A81C204C0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOBYHAJ12A6701BF1D</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SODACBL12A8C13C273</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SODDNQT12A6D4F5F7E</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SODXRTY12AB0180F3B</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOFGUAY12AB017B0A8</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOFRQTD12A81C233C0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOHQWYZ12A6D4FA701</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
</table>
[2000000 rows x 3 columns]<br/>Note: Only the head of the SFrame is printed.<br/>You can use print_rows(num_rows=m, num_columns=n) to print more rows and columns.
</div>




```python
usage_data.rename({'X1':'user_id', 'X2':'song_id', 'X3':'listen_count'})
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">user_id</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">song_id</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">listen_count</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOAKIMP12A8C130995</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOBBMDR12A8C13253B</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOBXHDL12A81C204C0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOBYHAJ12A6701BF1D</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SODACBL12A8C13C273</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SODDNQT12A6D4F5F7E</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SODXRTY12AB0180F3B</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOFGUAY12AB017B0A8</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOFRQTD12A81C233C0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">b80344d063b5ccb3212f76538<br>f3d9e43d87dca9e ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOHQWYZ12A6D4FA701</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
</table>
[2000000 rows x 3 columns]<br/>Note: Only the head of the SFrame is printed.<br/>You can use print_rows(num_rows=m, num_columns=n) to print more rows and columns.
</div>




```python
len(songs[songs['year'] == 0])
```




    484424




```python
songs['year'].sketch_summary()
```




    
    +--------------------+---------------+----------+
    |        item        |     value     | is exact |
    +--------------------+---------------+----------+
    |       Length       |    1000000    |   Yes    |
    |        Min         |      0.0      |   Yes    |
    |        Max         |     2011.0    |   Yes    |
    |        Mean        |  1030.325652  |   Yes    |
    |        Sum         |  1030325652.0 |   Yes    |
    |      Variance      | 997490.582407 |   Yes    |
    | Standard Deviation | 998.744503067 |   Yes    |
    |  # Missing Values  |       0       |   Yes    |
    |  # unique values   |       90      |    No    |
    +--------------------+---------------+----------+
    
    Most frequent items:
    +-------+--------+-------+-------+-------+-------+-------+-------+-------+-------+
    | value |   0    |  2007 |  2006 |  2005 |  2008 |  2009 |  2004 |  2003 |  2002 |
    +-------+--------+-------+-------+-------+-------+-------+-------+-------+-------+
    | count | 484424 | 39414 | 37546 | 34960 | 34770 | 31051 | 29618 | 27389 | 23472 |
    +-------+--------+-------+-------+-------+-------+-------+-------+-------+-------+
    +-------+
    |  2001 |
    +-------+
    | 21604 |
    +-------+
    
    Quantiles: 
    +-----+-----+-----+-----+--------+--------+--------+--------+--------+
    |  0% |  1% |  5% | 25% |  50%   |  75%   |  95%   |  99%   |  100%  |
    +-----+-----+-----+-----+--------+--------+--------+--------+--------+
    | 0.0 | 0.0 | 0.0 | 0.0 | 1969.0 | 2002.0 | 2008.0 | 2009.0 | 2011.0 |
    +-----+-----+-----+-----+--------+--------+--------+--------+--------+




```python
len(songs[songs['artist_name']].unique())
```




    999502




```python
len(songs[songs['release']].unique())
```




    999502




```python
len(songs[songs['song_id']].unique())
```




    999502




```python
songs_usage = songs.join(usage_data, 'song_id', 'inner')
```


```python
len(songs_usage)
```




    2086946




```python
#songs_usage.remove_column('year')
songs_usage = songs_usage.sort('listen_count', ascending= False)
```


```python
songs_usage.head(2)
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">song_id</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">title</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">release</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">artist_name</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">year</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOFCGSE12AF72A674F</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Starshine</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Gorillaz</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Gorillaz</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2000</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">SOUAGPQ12A8AE47B3A</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Crack Under Pressure</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Stress related / Live and<br>learn ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Righteous Pigs</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1998</td>
    </tr>
</table>
<table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">user_id</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">listen_count</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2213</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">50996bbabb6f7857bf0c80194<br>35b5246a0e45cfd ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">920</td>
    </tr>
</table>
[2 rows x 7 columns]<br/>
</div>




```python
Gorillaz = songs_usage[songs_usage['artist_name'] == 'Gorillaz']
```


```python
len(Gorillaz['user_id'].unique())
```




    2693




```python
len(songs_usage['user_id'].unique())
```




    76353




```python
popular_artist = songs_usage.groupby(key_columns='artist_name', operations={'total_count': graphlab.aggregate.SUM('listen_count')})
```


```python
popular_artist.sort('total_count', ascending = False)
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">artist_name</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">total_count</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Kings Of Leon</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">86031</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Coldplay</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">78540</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Florence + The Machine</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">60066</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Dwight Yoakam</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">54136</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Björk</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">53814</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">The Black Keys</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">52220</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Muse</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">52136</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Justin Bieber</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">50376</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Jack Johnson</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">48487</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Eminem</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">41754</td>
    </tr>
</table>
[3378 rows x 2 columns]<br/>Note: Only the head of the SFrame is printed.<br/>You can use print_rows(num_rows=m, num_columns=n) to print more rows and columns.
</div>




```python
popular_title = songs_usage.groupby(key_columns='title', operations={'total_count': graphlab.aggregate.SUM('listen_count')})
```


```python
popular_title.sort('total_count', ascending = False)
```




<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">title</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">total_count</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">You're The One</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">54915</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Undo</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">49253</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Revelry</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">41418</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Horn Concerto No. 4 in E<br>flat K495: II. Romance ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">31153</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Sehr kosmisch</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">31036</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Dog Days Are Over (Radio<br>Edit) ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">26663</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Use Somebody</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">22140</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Secrets</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">22100</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Canada</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">21019</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Invalid</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">19645</td>
    </tr>
</table>
[9593 rows x 2 columns]<br/>Note: Only the head of the SFrame is printed.<br/>You can use print_rows(num_rows=m, num_columns=n) to print more rows and columns.
</div>



### Song Recommender Model


```python
train_data,test_data = songs_usage.random_split(.8,seed=0)
```


```python
popularity_model = graphlab.popularity_recommender.create(train_data,user_id='user_id',item_id='artist_name')
```


<pre>Recsys training: model = popularity</pre>



<pre>Warning: Ignoring columns song_id, title, release, listen_count;</pre>



<pre>    To use one of these as a target column, set target = <column_name></pre>



<pre>    and use a method that allows the use of a target.</pre>



<pre>Preparing data set.</pre>



<pre>    Data has 1669380 observations with 76117 users and 3378 items.</pre>



<pre>    Data prepared in: 3.37624s</pre>



<pre>1669380 observations to process; with 3378 unique items.</pre>



```python
popularity_model.summary()
```

    Class                            : PopularityRecommender
    
    Schema
    ------
    User ID                          : user_id
    Item ID                          : artist_name
    Target                           : None
    Additional observation features  : 0
    User side features               : []
    Item side features               : []
    
    Statistics
    ----------
    Number of observations           : 1669380
    Number of users                  : 76117
    Number of items                  : 3378
    
    Training summary
    ----------------
    Training time                    : 0.0031
    
    Model Parameters
    ----------------
    Model class                      : PopularityRecommender
    



```python
results = popularity_model.recommend()
results
```


<pre>recommendations finished on 1000/76117 queries. users per second: 28458.4</pre>



<pre>recommendations finished on 2000/76117 queries. users per second: 33400.7</pre>



<pre>recommendations finished on 3000/76117 queries. users per second: 22928.2</pre>



<pre>recommendations finished on 4000/76117 queries. users per second: 21923</pre>



<pre>recommendations finished on 5000/76117 queries. users per second: 22973.3</pre>



<pre>recommendations finished on 6000/76117 queries. users per second: 24560</pre>



<pre>recommendations finished on 7000/76117 queries. users per second: 24577.2</pre>



<pre>recommendations finished on 8000/76117 queries. users per second: 24886</pre>



<pre>recommendations finished on 9000/76117 queries. users per second: 25124.2</pre>



<pre>recommendations finished on 10000/76117 queries. users per second: 25126.1</pre>



<pre>recommendations finished on 11000/76117 queries. users per second: 25019.6</pre>



<pre>recommendations finished on 12000/76117 queries. users per second: 25270.9</pre>



<pre>recommendations finished on 13000/76117 queries. users per second: 25185.1</pre>



<pre>recommendations finished on 14000/76117 queries. users per second: 25403.2</pre>



<pre>recommendations finished on 15000/76117 queries. users per second: 25097.6</pre>



<pre>recommendations finished on 16000/76117 queries. users per second: 24907.2</pre>



<pre>recommendations finished on 17000/76117 queries. users per second: 24506.6</pre>



<pre>recommendations finished on 18000/76117 queries. users per second: 24751</pre>



<pre>recommendations finished on 19000/76117 queries. users per second: 24702</pre>



<pre>recommendations finished on 20000/76117 queries. users per second: 25034.2</pre>



<pre>recommendations finished on 21000/76117 queries. users per second: 25001.5</pre>



<pre>recommendations finished on 22000/76117 queries. users per second: 25272.9</pre>



<pre>recommendations finished on 23000/76117 queries. users per second: 24969.9</pre>



<pre>recommendations finished on 24000/76117 queries. users per second: 25112.5</pre>



<pre>recommendations finished on 25000/76117 queries. users per second: 25083.2</pre>



<pre>recommendations finished on 26000/76117 queries. users per second: 25175.3</pre>



<pre>recommendations finished on 27000/76117 queries. users per second: 25486.9</pre>



<pre>recommendations finished on 28000/76117 queries. users per second: 25572.7</pre>



<pre>recommendations finished on 29000/76117 queries. users per second: 25375.5</pre>



<pre>recommendations finished on 30000/76117 queries. users per second: 25699.1</pre>



<pre>recommendations finished on 31000/76117 queries. users per second: 25868.2</pre>



<pre>recommendations finished on 32000/76117 queries. users per second: 26142</pre>



<pre>recommendations finished on 33000/76117 queries. users per second: 26255.7</pre>



<pre>recommendations finished on 34000/76117 queries. users per second: 26239.7</pre>



<pre>recommendations finished on 35000/76117 queries. users per second: 26293.6</pre>



<pre>recommendations finished on 36000/76117 queries. users per second: 26575.7</pre>



<pre>recommendations finished on 37000/76117 queries. users per second: 26764.3</pre>



<pre>recommendations finished on 38000/76117 queries. users per second: 27021.5</pre>



<pre>recommendations finished on 39000/76117 queries. users per second: 27119.9</pre>



<pre>recommendations finished on 40000/76117 queries. users per second: 27425.1</pre>



<pre>recommendations finished on 41000/76117 queries. users per second: 27506.8</pre>



<pre>recommendations finished on 42000/76117 queries. users per second: 27687</pre>



<pre>recommendations finished on 43000/76117 queries. users per second: 27777.4</pre>



<pre>recommendations finished on 44000/76117 queries. users per second: 28003.2</pre>



<pre>recommendations finished on 45000/76117 queries. users per second: 28104.3</pre>



<pre>recommendations finished on 46000/76117 queries. users per second: 28350.7</pre>



<pre>recommendations finished on 47000/76117 queries. users per second: 28414.6</pre>



<pre>recommendations finished on 48000/76117 queries. users per second: 28483.1</pre>



<pre>recommendations finished on 49000/76117 queries. users per second: 28673.1</pre>



<pre>recommendations finished on 50000/76117 queries. users per second: 28770.1</pre>



<pre>recommendations finished on 51000/76117 queries. users per second: 28988.7</pre>



<pre>recommendations finished on 52000/76117 queries. users per second: 29046.6</pre>



<pre>recommendations finished on 53000/76117 queries. users per second: 28850.9</pre>



<pre>recommendations finished on 54000/76117 queries. users per second: 28833.2</pre>



<pre>recommendations finished on 55000/76117 queries. users per second: 28570.9</pre>



<pre>recommendations finished on 56000/76117 queries. users per second: 28243.7</pre>



<pre>recommendations finished on 57000/76117 queries. users per second: 27958.2</pre>



<pre>recommendations finished on 58000/76117 queries. users per second: 28054.2</pre>



<pre>recommendations finished on 59000/76117 queries. users per second: 28009.5</pre>



<pre>recommendations finished on 60000/76117 queries. users per second: 27839.2</pre>



<pre>recommendations finished on 61000/76117 queries. users per second: 27895</pre>



<pre>recommendations finished on 62000/76117 queries. users per second: 27997.6</pre>



<pre>recommendations finished on 63000/76117 queries. users per second: 28132.3</pre>



<pre>recommendations finished on 64000/76117 queries. users per second: 28177.9</pre>



<pre>recommendations finished on 65000/76117 queries. users per second: 28163.9</pre>



<pre>recommendations finished on 66000/76117 queries. users per second: 28226.1</pre>



<pre>recommendations finished on 67000/76117 queries. users per second: 28326.9</pre>



<pre>recommendations finished on 68000/76117 queries. users per second: 28398.5</pre>



<pre>recommendations finished on 69000/76117 queries. users per second: 28429.6</pre>



<pre>recommendations finished on 70000/76117 queries. users per second: 28418.2</pre>



<pre>recommendations finished on 71000/76117 queries. users per second: 28559.4</pre>



<pre>recommendations finished on 72000/76117 queries. users per second: 28753.9</pre>



<pre>recommendations finished on 73000/76117 queries. users per second: 28941.7</pre>



<pre>recommendations finished on 74000/76117 queries. users per second: 28985.4</pre>



<pre>recommendations finished on 75000/76117 queries. users per second: 28944.4</pre>



<pre>recommendations finished on 76000/76117 queries. users per second: 28708.6</pre>





<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">user_id</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">artist_name</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">score</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">rank</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Coldplay</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">26055.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Kings Of Leon</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">20962.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">The Black Keys</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">15855.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">3</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Jack Johnson</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">15617.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Florence + The Machine</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">14578.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Justin Bieber</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">13342.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">6</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Daft Punk</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">11922.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">7</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Taylor Swift</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">10578.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">8</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Train</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">10018.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">9</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Lily Allen</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">9585.0</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">10</td>
    </tr>
</table>
[761170 rows x 4 columns]<br/>Note: Only the head of the SFrame is printed.<br/>You can use print_rows(num_rows=m, num_columns=n) to print more rows and columns.
</div>




```python
personalized_model = graphlab.item_similarity_recommender.create(train_data,
                                                                user_id='user_id',
                                                                item_id='artist_name')
```


<pre>Recsys training: model = item_similarity</pre>



<pre>Warning: Ignoring columns song_id, title, release, listen_count;</pre>



<pre>    To use one of these as a target column, set target = <column_name></pre>



<pre>    and use a method that allows the use of a target.</pre>



<pre>Preparing data set.</pre>



<pre>    Data has 1669380 observations with 76117 users and 3378 items.</pre>



<pre>    Data prepared in: 3.40664s</pre>



<pre>Training model from provided data.</pre>



<pre>Gathering per-item and per-user statistics.</pre>



<pre>+--------------------------------+------------+</pre>



<pre>| Elapsed Time (Item Statistics) | % Complete |</pre>



<pre>+--------------------------------+------------+</pre>



<pre>| 2.892ms                        | 1.25       |</pre>



<pre>| 94.289ms                       | 100        |</pre>



<pre>+--------------------------------+------------+</pre>



<pre>Setting up lookup tables.</pre>



<pre>Processing data in one pass using dense lookup tables.</pre>



<pre>+-------------------------------------+------------------+-----------------+</pre>



<pre>| Elapsed Time (Constructing Lookups) | Total % Complete | Items Processed |</pre>



<pre>+-------------------------------------+------------------+-----------------+</pre>



<pre>| 151.341ms                           | 0                | 0               |</pre>



<pre>| 761.801ms                           | 100              | 3378            |</pre>



<pre>+-------------------------------------+------------------+-----------------+</pre>



<pre>Finalizing lookup tables.</pre>



<pre>Generating candidate set for working with new users.</pre>



<pre>Finished training in 0.909761s</pre>



```python
graphlab_model = graphlab.recommender.create(train_data, user_id='user_id', item_id='artist_name') 
recs = graphlab_model.recommend()
recs
```


<pre>Recsys training: model = item_similarity</pre>



<pre>Warning: Ignoring columns song_id, title, release, listen_count;</pre>



<pre>    To use one of these as a target column, set target = <column_name></pre>



<pre>    and use a method that allows the use of a target.</pre>



<pre>Preparing data set.</pre>



<pre>    Data has 1669380 observations with 76117 users and 3378 items.</pre>



<pre>    Data prepared in: 4.20547s</pre>



<pre>Training model from provided data.</pre>



<pre>Gathering per-item and per-user statistics.</pre>



<pre>+--------------------------------+------------+</pre>



<pre>| Elapsed Time (Item Statistics) | % Complete |</pre>



<pre>+--------------------------------+------------+</pre>



<pre>| 13.053ms                       | 3.75       |</pre>



<pre>| 125.316ms                      | 100        |</pre>



<pre>+--------------------------------+------------+</pre>



<pre>Setting up lookup tables.</pre>



<pre>Processing data in one pass using dense lookup tables.</pre>



<pre>+-------------------------------------+------------------+-----------------+</pre>



<pre>| Elapsed Time (Constructing Lookups) | Total % Complete | Items Processed |</pre>



<pre>+-------------------------------------+------------------+-----------------+</pre>



<pre>| 204.004ms                           | 0                | 0               |</pre>



<pre>| 871.919ms                           | 100              | 3378            |</pre>



<pre>+-------------------------------------+------------------+-----------------+</pre>



<pre>Finalizing lookup tables.</pre>



<pre>Generating candidate set for working with new users.</pre>



<pre>Finished training in 1.08996s</pre>



<pre>recommendations finished on 1000/76117 queries. users per second: 29955.4</pre>



<pre>recommendations finished on 2000/76117 queries. users per second: 26624.8</pre>



<pre>recommendations finished on 3000/76117 queries. users per second: 26116.3</pre>



<pre>recommendations finished on 4000/76117 queries. users per second: 25808</pre>



<pre>recommendations finished on 5000/76117 queries. users per second: 22390.1</pre>



<pre>recommendations finished on 6000/76117 queries. users per second: 20755.2</pre>



<pre>recommendations finished on 7000/76117 queries. users per second: 19203.8</pre>



<pre>recommendations finished on 8000/76117 queries. users per second: 18318.8</pre>



<pre>recommendations finished on 9000/76117 queries. users per second: 17925.8</pre>



<pre>recommendations finished on 10000/76117 queries. users per second: 16729.9</pre>



<pre>recommendations finished on 11000/76117 queries. users per second: 16070.5</pre>



<pre>recommendations finished on 12000/76117 queries. users per second: 16236.5</pre>



<pre>recommendations finished on 13000/76117 queries. users per second: 16307.1</pre>



<pre>recommendations finished on 14000/76117 queries. users per second: 16292.6</pre>



<pre>recommendations finished on 15000/76117 queries. users per second: 16045.5</pre>



<pre>recommendations finished on 16000/76117 queries. users per second: 16289.1</pre>



<pre>recommendations finished on 17000/76117 queries. users per second: 16463.4</pre>



<pre>recommendations finished on 18000/76117 queries. users per second: 16634.9</pre>



<pre>recommendations finished on 19000/76117 queries. users per second: 16506.5</pre>



<pre>recommendations finished on 20000/76117 queries. users per second: 16627</pre>



<pre>recommendations finished on 21000/76117 queries. users per second: 16780.5</pre>



<pre>recommendations finished on 22000/76117 queries. users per second: 16857.6</pre>



<pre>recommendations finished on 23000/76117 queries. users per second: 16885.2</pre>



<pre>recommendations finished on 24000/76117 queries. users per second: 17126</pre>



<pre>recommendations finished on 25000/76117 queries. users per second: 17317.2</pre>



<pre>recommendations finished on 26000/76117 queries. users per second: 17561</pre>



<pre>recommendations finished on 27000/76117 queries. users per second: 17732.1</pre>



<pre>recommendations finished on 28000/76117 queries. users per second: 17907</pre>



<pre>recommendations finished on 29000/76117 queries. users per second: 17688.4</pre>



<pre>recommendations finished on 30000/76117 queries. users per second: 17545.1</pre>



<pre>recommendations finished on 31000/76117 queries. users per second: 17433.5</pre>



<pre>recommendations finished on 32000/76117 queries. users per second: 17553.2</pre>



<pre>recommendations finished on 33000/76117 queries. users per second: 17627.4</pre>



<pre>recommendations finished on 34000/76117 queries. users per second: 17612.4</pre>



<pre>recommendations finished on 35000/76117 queries. users per second: 17759.1</pre>



<pre>recommendations finished on 36000/76117 queries. users per second: 17913.6</pre>



<pre>recommendations finished on 37000/76117 queries. users per second: 18107.2</pre>



<pre>recommendations finished on 38000/76117 queries. users per second: 18226.9</pre>



<pre>recommendations finished on 39000/76117 queries. users per second: 18294.8</pre>



<pre>recommendations finished on 40000/76117 queries. users per second: 18427.2</pre>



<pre>recommendations finished on 41000/76117 queries. users per second: 18492.2</pre>



<pre>recommendations finished on 42000/76117 queries. users per second: 18556.5</pre>



<pre>recommendations finished on 43000/76117 queries. users per second: 18592.2</pre>



<pre>recommendations finished on 44000/76117 queries. users per second: 18414.1</pre>



<pre>recommendations finished on 45000/76117 queries. users per second: 18567.2</pre>



<pre>recommendations finished on 46000/76117 queries. users per second: 18670.7</pre>



<pre>recommendations finished on 47000/76117 queries. users per second: 18752.1</pre>



<pre>recommendations finished on 48000/76117 queries. users per second: 18766.3</pre>



<pre>recommendations finished on 49000/76117 queries. users per second: 18858.7</pre>



<pre>recommendations finished on 50000/76117 queries. users per second: 18901.5</pre>



<pre>recommendations finished on 51000/76117 queries. users per second: 19045.3</pre>



<pre>recommendations finished on 52000/76117 queries. users per second: 19215.7</pre>



<pre>recommendations finished on 53000/76117 queries. users per second: 19337.2</pre>



<pre>recommendations finished on 54000/76117 queries. users per second: 19431.9</pre>



<pre>recommendations finished on 55000/76117 queries. users per second: 19537.5</pre>



<pre>recommendations finished on 56000/76117 queries. users per second: 19511.3</pre>



<pre>recommendations finished on 57000/76117 queries. users per second: 19547.3</pre>



<pre>recommendations finished on 58000/76117 queries. users per second: 19687</pre>



<pre>recommendations finished on 59000/76117 queries. users per second: 19751</pre>



<pre>recommendations finished on 60000/76117 queries. users per second: 19862.7</pre>



<pre>recommendations finished on 61000/76117 queries. users per second: 19847.5</pre>



<pre>recommendations finished on 62000/76117 queries. users per second: 19919.7</pre>



<pre>recommendations finished on 63000/76117 queries. users per second: 20071</pre>



<pre>recommendations finished on 64000/76117 queries. users per second: 20200.7</pre>



<pre>recommendations finished on 65000/76117 queries. users per second: 20326.5</pre>



<pre>recommendations finished on 66000/76117 queries. users per second: 20448.6</pre>



<pre>recommendations finished on 67000/76117 queries. users per second: 20569.4</pre>



<pre>recommendations finished on 68000/76117 queries. users per second: 20707</pre>



<pre>recommendations finished on 69000/76117 queries. users per second: 20829.3</pre>



<pre>recommendations finished on 70000/76117 queries. users per second: 20977.5</pre>



<pre>recommendations finished on 71000/76117 queries. users per second: 21080.6</pre>



<pre>recommendations finished on 72000/76117 queries. users per second: 21206.1</pre>



<pre>recommendations finished on 73000/76117 queries. users per second: 21280</pre>



<pre>recommendations finished on 74000/76117 queries. users per second: 21392.9</pre>



<pre>recommendations finished on 75000/76117 queries. users per second: 21498.5</pre>



<pre>recommendations finished on 76000/76117 queries. users per second: 21496.9</pre>





<div style="max-height:1000px;max-width:1500px;overflow:auto;"><table frame="box" rules="cols">
    <tr>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">user_id</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">artist_name</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">score</th>
        <th style="padding-left: 1em; padding-right: 1em; text-align: center">rank</th>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Coldplay</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0253377683619</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">1</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Daft Punk</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0241970343793</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">2</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Kings Of Leon</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0230106914297</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">3</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Florence + The Machine</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0209213114799</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">4</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">MGMT</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0204066076177</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">5</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Foo Fighters</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0198647684239</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">6</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">The White Stripes</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0191185880215</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">7</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">OneRepublic</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0188645948755</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">8</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">Cage The Elephant</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0188116494645</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">9</td>
    </tr>
    <tr>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">d13609d62db6df876d3cc3882<br>25478618bb7b912 ...</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">3 Doors Down</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">0.0185802515517</td>
        <td style="padding-left: 1em; padding-right: 1em; text-align: center; vertical-align: top">10</td>
    </tr>
</table>
[761170 rows x 4 columns]<br/>Note: Only the head of the SFrame is printed.<br/>You can use print_rows(num_rows=m, num_columns=n) to print more rows and columns.
</div>




```python
model_performance = graphlab.compare(test_data, [popularity_model, personalized_model], user_sample=0.05)
graphlab.show_comparison(model_performance,[popularity_model, personalized_model])

```

    compare_models: using 3445 users to estimate model performance
    PROGRESS: Evaluate model M0



<pre>recommendations finished on 1000/3445 queries. users per second: 5393.77</pre>



<pre>recommendations finished on 2000/3445 queries. users per second: 6152.2</pre>



<pre>recommendations finished on 3000/3445 queries. users per second: 6403.7</pre>


    
    Precision and recall summary statistics by cutoff
    +--------+-----------------+------------------+
    | cutoff |  mean_precision |   mean_recall    |
    +--------+-----------------+------------------+
    |   1    | 0.0182873730044 | 0.00347721333883 |
    |   2    | 0.0166908563135 | 0.00719455214407 |
    |   3    | 0.0139332365747 | 0.00873307108985 |
    |   4    | 0.0140783744557 | 0.0108565688114  |
    |   5    | 0.0142235123367 | 0.0129338670986  |
    |   6    | 0.0141267537494 | 0.0153055131349  |
    |   7    | 0.0140161725067 | 0.0181405854226  |
    |   8    | 0.0134252539913 | 0.0196901077563  |
    |   9    | 0.0131269150137 | 0.0219795485638  |
    |   10   | 0.0133236574746 | 0.0248830517318  |
    +--------+-----------------+------------------+
    [10 rows x 3 columns]
    
    PROGRESS: Evaluate model M1



<pre>recommendations finished on 1000/3445 queries. users per second: 4885.46</pre>



<pre>recommendations finished on 2000/3445 queries. users per second: 5143.83</pre>



<pre>recommendations finished on 3000/3445 queries. users per second: 5261.97</pre>


    
    Precision and recall summary statistics by cutoff
    +--------+-----------------+-----------------+
    | cutoff |  mean_precision |   mean_recall   |
    +--------+-----------------+-----------------+
    |   1    |  0.104499274311 | 0.0229988695323 |
    |   2    | 0.0851959361393 | 0.0367935629407 |
    |   3    | 0.0728592162554 |  0.046158201317 |
    |   4    | 0.0648766328012 | 0.0543249517279 |
    |   5    | 0.0599709724238 | 0.0612472047074 |
    |   6    | 0.0556845670053 | 0.0684946196467 |
    |   7    | 0.0514617458014 | 0.0743067258816 |
    |   8    | 0.0481132075472 | 0.0798959343628 |
    |   9    | 0.0458635703919 | 0.0861702736641 |
    |   10   | 0.0434252539913 | 0.0906136532461 |
    +--------+-----------------+-----------------+
    [10 rows x 3 columns]
    
    Model compare metric: precision_recall





```python

```

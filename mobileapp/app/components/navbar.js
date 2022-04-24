import { useNavigation } from '@react-navigation/native';
import * as React from 'react';
import { Appbar, BottomNavigation, Text } from 'react-native-paper';
import { theme } from '../utils/theme';

const MusicRoute = () => <Text>Music</Text>;

const AlbumsRoute = () => <Text>Albums</Text>;

const RecentsRoute = () => <Text>Recents</Text>;

const GroupRoute = () => <Text>Group</Text>;

export default function Navbar () {
  const [index, setIndex] = React.useState(0);
  const [routes] = React.useState([
    { key: 'wallet', title: 'Wallet', icon: 'wallet' },
    { key: 'co2', title: 'Emmissions', icon: 'leaf' },
    { key: 'settings', title: 'Settings', icon: 'cog' },
    { key: 'group', title: 'Group', icon: 'account-group' },
  ]);

  const navigation = useNavigation();

  return (
    <Appbar style={{backgroundColor:theme.primary, position:'absolute', bottom:0, width:'100%', justifyContent:'space-evenly'}}>
   <Appbar.Action
     icon="trophy"
     onPress={() => navigation.navigate('Score')}
    />
    <Appbar.Action icon="leaf" onPress={() => console.log('Pressed mail')} />
    <Appbar.Action icon="account-group" onPress={() => console.log('Pressed label')} />
    <Appbar.Action
      icon="cog"
      onPress={() => console.log('Pressed delete')}
    />
  </Appbar>
  );
};


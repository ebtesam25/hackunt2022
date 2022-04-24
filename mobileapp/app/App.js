import { StatusBar } from 'expo-status-bar';
import { StyleSheet, Text, View } from 'react-native';
import { NavigationContainer } from '@react-navigation/native';
import { createStackNavigator } from '@react-navigation/stack';
import Register from './screens/register';
import Emmissions from './screens/selectType';
import SelectSub from './screens/selectSub';
import AddEmission from './screens/addEmission';
import Group from './screens/group';
import Scores from './screens/scores';




const Stack = createStackNavigator();

function ScreenStack() {
  return (
    <Stack.Navigator>
      <Stack.Screen 
        name="Register" 
        component={Register} 
        options={{ headerShown: false}} 
      />
      <Stack.Screen 
        name="Emmission" 
        component={Emmissions} 
        options={{ headerShown: false}} 
      />
      <Stack.Screen 
        name="SelectSub" 
        component={SelectSub} 
        options={{ headerShown: false}} 
      />
      <Stack.Screen 
        name="Add" 
        component={AddEmission} 
        options={{ headerShown: false}} 
      />
      <Stack.Screen 
        name="Group" 
        component={Group} 
        options={{ headerShown: false}} 
      />
      <Stack.Screen 
        name="Score" 
        component={Scores} 
        options={{ headerShown: false}} 
      />
    </Stack.Navigator>
  );
}

export default function App() {
  return (
    <NavigationContainer>
      <ScreenStack />
    </NavigationContainer>
  );
}
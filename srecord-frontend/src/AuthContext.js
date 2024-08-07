import React, { createContext } from 'react';

export const AuthContext = createContext();

export const AuthProvider = ({ children, value }) => (
    <AuthContext.Provider value={value}>
        {children}
    </AuthContext.Provider>
);
